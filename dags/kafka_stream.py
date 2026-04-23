import uuid
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
#here we imported the necessary libraries

default_args ={
    'owner' : 'airscholar',
    'start_date' : datetime(2026, 4,17,4,00)
#here we say that start scheduling this DAG from this date and time
}
#THIS EXECUTES FIRST. THIS IS EXTRACT
def get_data():
    import requests  # to get data from api itself
    res = requests.get('https://randomuser.me/api/')
    res = res.json()
    res = res['results'][0]

    return res

#TRANSFORM PHASE. THIS IS TRANSFORM
#You are taking a complex, messy structure and flattening it into a single, clean record.
def format_data(res):
    data = {}  # this is where all the data we are gonna hold
    location = res['location']
    data['id'] = str(uuid.uuid4())
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']
    return data

#but the logic is ready for Kafka. THIS IS LOAD
def stream_data():
    import json
    from kafka import KafkaProducer
    import time
    import logging
    #print("raw data:", res)
    producer = KafkaProducer(bootstrap_servers = ['broker:29092'],max_block_ms = 5000) #this guy is gonna run on docker instance , so we change from local host 9092 to to broker 29092.
    curr_time = time.time() #here curr_time stores the start time.


    while True:                                 #infinite loop
        if time.time()  >  curr_time + 60:      # we wanna stream for 1minute. time.time() gives current time.
            break
        try:
            #send request to random user api ,get that data, format that data and send it to kafka queue or topic.
            res = get_data()  # fetch some raw data   # res stores return res value in it
            res = format_data(res)  # clean it   #replaces res value with return data value which is stored in res.
            producer.send('users_created', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue


#now we need to create or define the
#where user_automation is the task id
with DAG('user_automation',
         default_args = default_args,
         schedule_interval = '@daily',
         catchup = False) as dag:

    #now here we create a python operator
    streaming_task = PythonOperator(
        task_id = 'stream_data_from_api',
        python_callable = stream_data
    )