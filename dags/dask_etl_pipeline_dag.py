# Importing libraries
from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import dask.dataframe as dd
from sqlalchemy import create_engine
from datetime import datetime

# Defining the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

# Initializing the DAG
dag = DAG(
    'dask_etl_project_dag',
    default_args=default_args,
    description='Small ETL project using Dask DataFrame and Airflow',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False
)

# Function to extract data from MySQL
def extract_data():
    connection_params = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'ashiqur',
        'database': 'supermarket'
    }
    engine = create_engine(f"mysql+pymysql://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}")
    
    orders_df = dd.read_sql_table('orders', engine, index_col='order_id')
    products_df = dd.read_sql_table('products', engine, index_col='product_id')
    departments_df = dd.read_sql_table('departments', engine, index_col='department_id')
    
    return orders_df, products_df, departments_df

# Function to transform data 
def transform_data(orders_df, products_df, departments_df):
    merged_df = dd.merge(products_df, departments_df, on='department_id')
    return merged_df

# Function to load transformed data 
def load_data(merged_df, orders_df):
    db_settings = {
        'dbname': 'newdb',
        'user': 'root',
        'password': 'ashiqur',
        'host': 'localhost',
        'port': 3306
    }
    engine_uri = f"mysql+pymysql://{db_settings['user']}:{db_settings['password']}@{db_settings['host']}:{db_settings['port']}/{db_settings['dbname']}"
    
    merged_df.compute().to_sql('new_product_data', engine_uri, if_exists='replace', index=False)
    orders_df.compute().to_sql('new_order_data', engine_uri, if_exists='replace', index=False)

# Defining tasks in the DAG
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    op_kwargs={'orders_df': extract_task.output[0], 'products_df': extract_task.output[1], 'departments_df': extract_task.output[2]},
    dag=dag
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    op_kwargs={'merged_df': transform_task.output, 'orders_df': extract_task.output[0]},
    dag=dag
)

# Setting task dependencies
extract_task >> transform_task >> load_task
