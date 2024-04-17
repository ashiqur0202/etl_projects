# Project Setup Guide

This guide provides step-by-step instructions to set up your project environment using Docker, VSCode, and Docker Compose for Apache Airflow.

## Steps to Set Up the Project

### 1. Get Docker Desktop

If you haven't installed Docker yet, you can download it from [Docker's official website](https://www.docker.com/products/docker-desktop).

### 2. Get Visual Studio Code (VSCode)

If you haven't installed VSCode, you can download it from [VSCode's official website](https://code.visualstudio.com/).

### 3. Get Docker Compose File

[Download the Docker Compose file](https://airflow.apache.org/docs/apache-airflow/2.9.0/docker-compose.yaml) for project.


### 4. Create `.env` File

Create a `.env` file in the same directory as your Docker Compose file and add the following environment variables:


- AIRFLOW_IMAGE_NAME=apache/airflow:2.9.0
- AIRFLOW_UID=50000


### 5. Start Docker Compose
Run the following command to start the Docker Compose services:

- docker-compose up -d


### 6. Access Airflow Web UI

After the services are up and running, you can access the Airflow Web UI at:
http://localhost:8080

---

## Additional Notes
docker --version
docker-compose --version

get docker 
get vscode

get docker compose file

.env file and

AIRFLOW_IMAGE_NAME=apache/airflow:2.9.0
AIRFLOW_UID=50000

docker-compose up -d

localhost:8080


Troubleshoots
docker-compose ps
docker logs materials_name_of_the_container
docker-compose down
docker-compose up -d

docker volume prune
docker-compose up -d

### Stop the Docker Containers
docker compose down
### Verify Containers are Stopped
docker ps
### Start the Docker Containers
docker compose up -d
### Verify Containers are Running
docker ps

### Logs and Monitoring
docker-compose logs -f

### Updating Airflow Configuration or DAGs
docker-compose down
docker-compose build
docker-compose up -d