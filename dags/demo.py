# from airflow import DAG
# from airflow.providers.mysql.operators.mysql import MySqlOperator
# from airflow.operators.python_operator import PythonOperator
# from airflow.utils.dates import days_ago
# import dask.dataframe as dd
# from sqlalchemy import create_engine

# # Define the default arguments for the DAG
# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1
# }

# # Initialize the DAG
# dag = DAG(
#     'demo_dask_etl_project_dag',
#     default_args=default_args,
#     description='Small ETL project using Dask DataFrame and Airflow',
#     schedule_interval=None,
#     start_date=days_ago(1),
#     catchup=False
# )

# # # Function to extract data from MySQL
# # def extract_data():
# #     # MySQL source connection settings
# #     source_db_settings = {
# #         'dbname': 'adventureworks',
# #         'user': 'root',
# #         'password': 'ashiqur',
# #         'host': 'localhost',
# #         'port': 3306
# #     }

# #     # Create SQLAlchemy source engine
# #     source_engine = create_engine(f"mysql+pymysql://{source_db_settings['user']}:{source_db_settings['password']}@{source_db_settings['host']}:{source_db_settings['port']}/{source_db_settings['dbname']}")

# #     # Read data from source MySQL into Dask DataFrame
# #     df = dd.read_sql_table('sales', source_engine, index_col='MyUnknownColumn', npartitions=10)
    
# #     return df

# # # Function to transform data
# # def transform_data(df):
# #     # Transform data (Example: Convert column to uppercase)
# #     # df['your_column_name'] = df['your_column_name'].str.upper()
    
# #     return df

# # # Function to load data into MySQL
# # def load_data(df):
# #     # MySQL destination connection settings
# #     dest_db_settings = {
# #         'dbname': 'destination_db',
# #         'user': 'root',
# #         'password': 'ashiqur',
# #         'host': 'localhost',
# #         'port': 3306
# #     }

# #     # Create SQLAlchemy destination engine
# #     dest_engine = create_engine(f"mysql+pymysql://{dest_db_settings['user']}:{dest_db_settings['password']}@{dest_db_settings['host']}:{dest_db_settings['port']}/{dest_db_settings['dbname']}")

# #     # Write the transformed data to destination MySQL
# #     df.to_sql('transformed_table', dest_engine, if_exists='replace', index=False)

# # # Define tasks in the DAG
# # extract_data_task = PythonOperator(
# #     task_id='extract_data_from_mysql',
# #     python_callable=extract_data,
# #     dag=dag
# # )

# # transform_data_task = PythonOperator(
# #     task_id='transform_data',
# #     python_callable=transform_data,
# #     dag=dag
# # )

# # load_data_task = PythonOperator(
# #     task_id='load_data_to_mysql',
# #     python_callable=load_data,
# #     provide_context=True,
# #     dag=dag
# # )

# # # Set task dependencies
# # extract_data_task >> transform_data_task >> load_data_task
