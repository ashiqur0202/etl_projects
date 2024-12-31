# ETL Projects

This repository contains two ETL (Extract, Transform, Load) projects developed using different technologies:

1. A small ETL project using Dask DataFrame and Airflow.
2. A similar project using PySpark and Airflow.

## Table of Contents

- [ETL Projects](#etl-projects)
  - [Table of Contents](#table-of-contents)
  - [Technologies Used](#technologies-used)
  - [Project Descriptions](#project-descriptions)
  - [Setup and Installation](#setup-and-installation)
    - [Prerequisites](#prerequisites)
    - [Installation Steps](#installation-steps)
  - [Usage](#usage)
    - [Dask DataFrame and Airflow Project](#dask-dataframe-and-airflow-project)
    - [PySpark and Airflow Project](#pyspark-and-airflow-project)
  - [Contributing](#contributing)
  - [License](#license)

## Technologies Used

- Dask DataFrame
- PySpark
- Apache Airflow

## Project Descriptions

### 1. Dask DataFrame and Airflow Project

This project demonstrates a small ETL pipeline using Dask DataFrame and Apache Airflow. It includes tasks for data extraction, transformation, and loading using custom operators and helpers.

### 2. PySpark and Airflow Project

This project is similar to the Dask DataFrame and Airflow project but uses PySpark for data processing instead of Dask DataFrame.

## Setup and Installation

### Prerequisites

- Python 3.x
- Apache Airflow
- Dask (for Dask DataFrame project)
- PySpark (for PySpark project)

### Installation Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/ashiqur0202/ETL-Projects.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ETL-Projects
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Dask DataFrame and Airflow Project

1. Navigate to the `dask_dataframe_airflow_project` directory:

    ```bash
    cd dask_dataframe_airflow_project
    ```

2. Run the Airflow web server:

    ```bash
    airflow webserver -p 8080
    ```

3. Trigger the DAG from the Airflow UI or using the following command:

    ```bash
    airflow dags trigger etl_pipeline_dag
    ```

### PySpark and Airflow Project

1. Navigate to the `pyspark_airflow_project` directory:

    ```bash
    cd pyspark_airflow_project
    ```

2. Run the Airflow web server:

    ```bash
    airflow webserver -p 8080
    ```

3. Trigger the DAG from the Airflow UI or using the following command:

    ```bash
    airflow dags trigger etl_pipeline_dag
    ```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
