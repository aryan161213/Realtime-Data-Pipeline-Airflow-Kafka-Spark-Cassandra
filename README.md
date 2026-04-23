## Table of Contents

- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Core Components](#core-components)
- [Technologies Used](#technologies-used)
- [Key Features](#key-features)
- [Project Workflow](#project-workflow)
- [Images](#images)

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

---

### **Core Components**

* **Data Source**: Utilizing the Random User API to generate high-fidelity, mock user profiles in JSON format.
* **Orchestration**: Apache Airflow serves as the pipeline's backbone, managing task dependencies and scheduling, with PostgreSQL maintaining the state and metadata.
* **Stream Ingestion**: Apache Kafka (managed by Zookeeper) handles the high-throughput ingestion, decoupling the API source from the processing engine.
* **Governance & Monitoring**: Schema Registry enforces data contracts between producers and consumers, while the Control Center provides a centralized UI for cluster observability.
* **Distributed Processing**: Apache Spark utilizes a Master-Worker cluster to perform real-time, parallelized data transformations.
* **Data Sink**: Apache Cassandra acts as the final distributed storage layer, optimized for high-speed writes and scalable querying.


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

---

## Project Workflow
* **Ingestion & Orchestration**: Apache Airflow triggers a Python-based ingestion task, fetching raw JSON payloads from the Random User API.
* **Messaging & Buffering**: The raw data is produced into an Apache Kafka topic (users_created). Zookeeper ensures the cluster state is synchronized across brokers.
* **Stream Governance**: The Schema Registry validates the incoming data format, ensuring compatibility with downstream consumers.
* **Distributed Processing**: An Apache Spark Master detects the new stream, distributing processing tasks to Spark Workers that apply a strictly defined schema to the raw JSON.
* **Persistence**: The cleaned, structured data is "sunk" into an Apache Cassandra keyspace, making it immediately available for analytical queries.

---

## Images

<img width="1600" height="1012" alt="WhatsApp Image 2026-04-24 at 00 25 16 (1)" src="https://github.com/user-attachments/assets/3fd3c776-ca17-4a2c-bfba-b18f55b0d21a" />

---

<img width="1477" height="924" alt="WhatsApp Image 2026-04-24 at 00 25 16" src="https://github.com/user-attachments/assets/99ee29d6-b93a-4bbb-ab0f-abea92a4ab8b" />

---

<img width="1241" height="812" alt="WhatsApp Image 2026-04-24 at 00 25 16 (5)" src="https://github.com/user-attachments/assets/b97a235c-e1fa-4dcc-b066-5d53701fea17" />

---

<img width="1241" height="807" alt="WhatsApp Image 2026-04-24 at 00 25 16 (6)" src="https://github.com/user-attachments/assets/ae5a0ea4-5f2d-470f-b358-8dbf1d00b124" />

---

<img width="1380" height="904" alt="WhatsApp Image 2026-04-24 at 00 25 16 (7)" src="https://github.com/user-attachments/assets/6b702193-eccd-4f3d-958c-9e51dcb8737b" />

---

<img width="1280" height="831" alt="WhatsApp Image 2026-04-23 at 23 52 03" src="https://github.com/user-attachments/assets/3381d1c5-d761-4b0e-904f-7e8a07455da3" />

---

<img width="1280" height="831" alt="WhatsApp Image 2026-04-23 at 23 52 06" src="https://github.com/user-attachments/assets/787a1f24-dc96-4cdd-947a-eef6025a01f8" />

---

<img width="1280" height="831" alt="WhatsApp Image 2026-04-23 at 23 52 06 (1)" src="https://github.com/user-attachments/assets/5c2b29c1-426f-4fa6-8cd6-faaefc6f2ac8" />

---

<img width="1280" height="831" alt="WhatsApp Image 2026-04-23 at 23 52 04" src="https://github.com/user-attachments/assets/87fe4a97-cdd2-44bf-850a-c01b2dbd0f0c" />

---

<img width="1596" height="908" alt="WhatsApp Image 2026-04-23 at 23 58 51" src="https://github.com/user-attachments/assets/9585b066-ac1f-43cf-a0ff-20ce4bc2df6a" />

---

<img width="1094" height="692" alt="WhatsApp Image 2026-04-24 at 00 25 16 (3)" src="https://github.com/user-attachments/assets/769688e1-f1c0-477f-a14d-da15fd4ce58c" />

---

<img width="1600" height="1012" alt="WhatsApp Image 2026-04-24 at 00 03 17" src="https://github.com/user-attachments/assets/c4f0b37d-3e64-467f-8626-a2033b0edd8e" />

---

<img width="1600" height="1031" alt="WhatsApp Image 2026-04-24 at 00 03 17 (1)" src="https://github.com/user-attachments/assets/eb546371-c0b2-4cbb-9494-5a66882d621e" />

---

<img width="1600" height="1039" alt="WhatsApp Image 2026-04-24 at 00 13 03" src="https://github.com/user-attachments/assets/4ec42fd6-2d5f-4df2-a2aa-fa23ef7ee32d" />

---

<img width="2560" height="1662" alt="WhatsApp Image 2026-04-24 at 00 12 38 (1)" src="https://github.com/user-attachments/assets/d5795342-12d3-472a-9b99-ab64673177aa" />

---
<img width="1600" height="1039" alt="WhatsApp Image 2026-04-24 at 00 12 38 (2)" src="https://github.com/user-attachments/assets/9ab9a0b6-772d-4144-999b-6d5af2d1ff67" />

---

<img width="1600" height="959" alt="WhatsApp Image 2026-04-24 at 00 25 16 (2)" src="https://github.com/user-attachments/assets/e5ba099d-28e8-448e-a496-e4e69d3dcc00" />

---

<img width="1600" height="1039" alt="WhatsApp Image 2026-04-24 at 00 25 16 (4)" src="https://github.com/user-attachments/assets/5b2fafa7-1271-4974-b238-2ec79e5be5a9" />

---


