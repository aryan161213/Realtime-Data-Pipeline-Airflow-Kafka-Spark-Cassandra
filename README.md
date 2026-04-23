# Realtime-Data-Pipeline-Airflow-Kafka-Spark-Cassandra


## OVERVIEW
A real-time data engineering pipeline that fetches user data from a random API, orchestrates ingestion with Airflow, streams through Kafka, processes with PySpark, and stores in Cassandra—all containerized using Docker.

* **End-to-End Real-Time Pipeline**:Built a robust data engineering pipeline that simulates a production environment, transforming raw API data into structured, queryable insights in seconds.
* **Decoupled Distributed Architecture**: Leveraged a microservices-based approach where each component (Ingestion, Messaging, Processing, and Storage) is isolated within Docker containers, ensuring system resilience and easy scalability.
* **High-Velocity Ingestion**: Implemented Apache Airflow to orchestrate seamless data retrieval, using PostgreSQL as a reliable metadata backbone to track pipeline health and task execution.
* **Reliable Stream Management**: Utilized Apache Kafka paired with Zookeeper for high-throughput event streaming, incorporating Confluent Schema Registry to enforce data contracts and Control Center for real-time observability.
* **Distributed Computing Power**: Engineered a Spark Master-Worker cluster to handle parallelized data transformations, converting complex JSON payloads into cleaned, schema-validated formats at scale.
* **Scalable NoSQL Storage**: Finalized the pipeline by persisting high-volume processed data into Apache Cassandra, enabling low-latency lookups and high-availability storage for downstream analytics.


---

## System Architecture

<img width="3274" height="1221" alt="Data engineering architecture" src="https://github.com/user-attachments/assets/fce95803-4cdc-4f03-9043-af3a17358188" />

The project is designed with the following components:

* **Data Source**: We use randomuser.me API to generate random user data for our pipeline.
* **Apache Airflow**: Responsible for orchestrating the pipeline and storing fetched data in a PostgreSQL database.
* **Apache Kafka and Zookeeper**: Used for streaming data from PostgreSQL to the processing engine.
* **Control Center and Schema Registry**: Helps in monitoring and schema management of our Kafka streams.
* **Apache Spark**: For data processing with its master and worker nodes.
* **Cassandra**: Where the processed data will be stored.


---
## Technologies Used

* **Python**: Core language for pipeline logic, API interaction, and Spark transformations.
* **Apache Airflow**: Orchestrates the workflow; schedules the data ingestion from the API.
* **Apache Kafka**: Distributed message broker that handles real-time data ingestion.
* **Apache Spark**: Processes the data stream, applies the schema, and transforms the raw JSON.
* **Cassandra**: High-performance NoSQL database for final data persistence.
* **PostgreSQL**: Backend metadata store for Airflow, ensuring robust task scheduling.
* **Docker & Docker Compose**: Containerizes the entire stack for seamless deployment and scalability.

---

## Key Features

* **Fault-Tolerant Streaming**: The pipeline is designed to handle node failures (Kafka Brokers or Spark Workers) without data loss.
* **Schema Governance**: Uses Schema Registry to prevent "poison pills" (malformed data) from crashing the Spark processing layer.
* **Scalable Distributed Computing**: A dedicated Spark Master manages multiple workers, allowing the system to scale horizontally as data volume grows.
* **Real-Time Monitoring**: Integrated dashboards via Kafka Control Center allow for tracking consumer lag and system health.
* **Microservices Orchestration**: Fully containerized stack enabling one-command deployment of 7+ interconnected services.


