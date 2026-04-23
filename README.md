# Realtime-Data-Pipeline-Airflow-Kafka-Spark-Cassandra


## OVERVIEW
A real-time data engineering pipeline that fetches user data from a random API, orchestrates ingestion with Airflow, streams through Kafka, processes with PySpark, and stores in Cassandra—all containerized using Docker.
The project is designed with the following components:

Data Source: We use randomuser.me API to generate random user data for our pipeline.
Apache Airflow: Responsible for orchestrating the pipeline and storing fetched data in a PostgreSQL database.
Apache Kafka and Zookeeper: Used for streaming data from PostgreSQL to the processing engine.
Control Center and Schema Registry: Helps in monitoring and schema management of our Kafka streams.
Apache Spark: For data processing with its master and worker nodes.
Cassandra: Where the processed data will be stored.

---

## System Architecture

<img width="3274" height="1221" alt="Data engineering architecture" src="https://github.com/user-attachments/assets/fce95803-4cdc-4f03-9043-af3a17358188" />

---

## Technologies
* Apache Airflow
* Python
* Apache Kafka
* Apache Zookeeper
* Apache Spark
* Cassandra
* PostgreSQL
* Docker


