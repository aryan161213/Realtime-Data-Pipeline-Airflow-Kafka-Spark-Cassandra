'''stream data into cassandra'''

import logging
import datetime as datetime

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from click import option

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType


    #Creating a key space which is like a schema for cassandra before doing or initialising anything , to keep things structured.

def create_keyspace(session):
    #creating keyspace here
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS spark_streams
        WITH REPLICATION = {'class':'SimpleStrategy', 'replication_factor' : '1'}
    """)

    print("Keyspace created succesfully!")

def create_table(session):              #creating table here
    session.execute("""
        CREATE TABLE IF NOT EXISTS spark_streams.created_users(
            id UUID PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            gender TEXT,
            address TEXT,
            post_code TEXT,
            email TEXT,
            username TEXT,
            registered_date TEXT,
            phone TEXT,
            picture TEXT);
    """)
    print("Table created succesfully!")

def insert_data(session, **kwargs):  #**kwargs means accept any number of arguments
    #we do insertion logic here
    print("Inserting data...")


    id = kwargs.get('id')
    first_name = kwargs.get('first_name')
    last_name = kwargs.get('last_name')
    gender = kwargs.get('gender')
    address = kwargs.get('address')
    post_code = kwargs.get('post_code')
    email = kwargs.get('email')
    username = kwargs.get('username')
    registered_date = kwargs.get('registered_date')
    phone = kwargs.get('phone')
    picture = kwargs.get('picture')

    try:
        session.execute("""
            INSERT INTO spark_streams.created_users(id, first_name, last_name, gender, address, 
                post_code, email, username, dob, registered_date, phone, picture)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (id, first_name, last_name, gender, address, post_code, email, username, registered_date, phone, picture))
        logging.info(f"Data inserted for {first_name} {last_name}")
    except Exception as e:
        logging.error(f'could not insert data due to {e}')

def create_spark_connection():
    # connecting to spark
    s_conn = None            #ensures even if something fails s_conn exists as None at least
    try:
        s_conn = SparkSession.builder \
            .appName("SparkDataStreaming") \
            .config("spark.jars.packages",
                    "com.datastax.spark:spark-cassandra-connector_2.13:3.5.1," #we are joining with a comma both as config allows only 2  arguments to be passed.
                    "org.apache.spark:spark-sql-kafka-0-10_2.13:4.1.1"
            ) \
            .config("spark.cassandra.connection.host", "localhost") \
            .getOrCreate() #configuring hostname for cassandra
        s_conn.sparkContext.setLogLevel("ERROR") # this tells us that only show errors dont show anything else any warnings,any debug messages,etc
        logging.info("Spark connection created succesfully!") #just prints message
    except Exception as e:
        logging.error(f"Couldn't create spark connection due to exception {e}")

    return s_conn       #this is after except block , not within except block

def connect_to_kafka(s_conn):# we are telling spark how to read Streaming data from kafka
    spark_df = None
    try:
        # start reading live data  #where kafka is running on our device,#tells us to read from user_created topic only,#read from beginning
        spark_df = spark_conn.readStream \
            .format('kafka') \
            .option('kafka.bootstrap.servers', 'localhost:9092') \
            .option('subscribe', 'users_created') \
            .option('startingOffsets', 'earliest') \
            .load()
        logging.info("kafka dataframe created successfully")
    except Exception as e:
        logging.warning(f"kafka dataframe could not be created because: {e}")

    return spark_df



def create_cassandra_connection():
    #creating cassandra connection
    try:
        cluster = Cluster(['localhost'])
        cas_sess = cluster.connect()
        return cas_sess         #so here we return immediately after sucess as here variables maynot change mutliple times and less complex logic is involved here
        #logging.info("Cassandra connection created succesfully!")

    except Exception as e:
        logging.error(f"Couldn't create cassandra connection due to exception {e}")
        return None


def create_selection_df_from_kafka(spark_df):
    schema = StructType([
        StructField("id", StringType(), False),
        StructField("first_name", StringType(), False),
        StructField("last_name", StringType(), False),
        StructField("gender", StringType(), False),
        StructField("address", StringType(), False),
        StructField("post_code", StringType(), False),
        StructField("email", StringType(), False),
        StructField("username", StringType(), False),
        StructField("registered_date", StringType(), False),
        StructField("phone", StringType(), False),
        StructField("picture", StringType(), False)
    ])

    sel = spark_df.selectExpr("CAST(value AS STRING)") \
        .select(from_json(col('value'), schema).alias('data')).select("data.*")
    print(sel)

    return sel

if __name__ == "__main__":     #means that run this code only when the file is run directly ie python spark_stream.py
    #create spark connection
    spark_conn = create_spark_connection()

    if spark_conn is not None:     #only continue if spark has started succesfully
       #connect to kafka with spark connection
        df = connect_to_kafka(spark_conn)
        selection_df = create_selection_df_from_kafka(df)
        session = create_cassandra_connection() #now cassandra connects only if spark is ready

        if session is not None:
            create_keyspace(session)
            create_table(session)
            #insert_data(session)

            streaming_query = (selection_df.writeStream.format("org.apache.spark.sql.cassandra")
                               .option('checkpointLocation', '/tmp/checkpoint')
                               .option('keyspace', 'spark_streams')
                               .option('table', 'created_users')
                               .start())

            streaming_query.awaitTermination()