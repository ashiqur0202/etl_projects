## I
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
