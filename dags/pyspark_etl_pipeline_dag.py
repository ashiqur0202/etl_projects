# Importing libraries
from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder \
    .appName("PySpark_ETL") \
    .getOrCreate()

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

# Initialize the DAG
dag = DAG(
    'pyspark_etl_project_dag',
    default_args=default_args,
    description='Small ETL project using PySpark and Airflow',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False
)

# Function to extract data from MySQL
def extract_data():
    orders_df = spark.read.format("jdbc").options(
        url="jdbc:mysql://localhost:3306/supermarket",
        driver="com.mysql.jdbc.Driver",
        dbtable="orders",
        user="root",
        password="ashiqur"
    ).load()
    
    products_df = spark.read.format("jdbc").options(
        url="jdbc:mysql://localhost:3306/supermarket",
        driver="com.mysql.jdbc.Driver",
        dbtable="products",
        user="root",
        password="ashiqur"
    ).load()
    
    departments_df = spark.read.format("jdbc").options(
        url="jdbc:mysql://localhost:3306/supermarket",
        driver="com.mysql.jdbc.Driver",
        dbtable="departments",
        user="root",
        password="ashiqur"
    ).load()
    
    return orders_df, products_df, departments_df

# Function to transform data
def transform_data(**context):
    ti = context['ti']
    orders_df, products_df, departments_df = ti.xcom_pull(key=None, task_ids='extract_data')
    
    merged_df = products_df.join(departments_df, on='department_id')
    return merged_df

# Function to load transformed data into MySQL
def load_data(**context):
    ti = context['ti']
    merged_df = ti.xcom_pull(key=None, task_ids='transform_data')
    orders_df = ti.xcom_pull(key=None, task_ids='extract_data')[0]
    
    merged_df.write.format("jdbc").options(
        url="jdbc:mysql://localhost:3306/newdb",
        driver="com.mysql.jdbc.Driver",
        dbtable="new_product_data",
        user="root",
        password="ashiqur"
    ).mode("overwrite").save()
    
    orders_df.write.format("jdbc").options(
        url="jdbc:mysql://localhost:3306/newdb",
        driver="com.mysql.jdbc.Driver",
        dbtable="new_order_data",
        user="root",
        password="ashiqur"
    ).mode("overwrite").save()

# Define tasks in the DAG
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    provide_context=True,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    provide_context=True,
    dag=dag
)

# Set task dependencies
extract_task >> transform_task >> load_task

# Stop Spark session
spark.stop()
