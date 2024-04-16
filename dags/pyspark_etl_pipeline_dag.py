# from airflow import DAG
# from airflow.providers.mysql.operators.mysql import MySqlOperator
# from airflow.operators.python_operator import PythonOperator
# from airflow.utils.dates import days_ago
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import upper

# # Initialize Spark session
# spark = SparkSession.builder \
#     .appName("PySpark_ETL") \
#     .getOrCreate()

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
#     'pyspark_etl_pipeline_dag',
#     default_args=default_args,
#     description='Similar project using PySpark and Airflow',
#     schedule_interval=None,
#     # start_date=days_ago(1),
#     catchup=False
# )

# # Function to perform ETL using PySpark
# def perform_etl():
#     # Read data from MySQL into PySpark DataFrame
#     df = spark.read.format("jdbc").options(
#         url="jdbc:mysql://localhost:3306/adventureworks",
#         driver="com.mysql.jdbc.Driver",
#         dbtable="sales",
#         user="root",
#         password="ashiqur"
#     ).load()
    
#     # Transform data (Example: Convert column to uppercase)
#     df_transformed = df.withColumn("your_column_name", upper(df["your_column_name"]))
    
#     # Write the transformed data back to MySQL
#     df_transformed.write.format("jdbc").options(
#         url="jdbc:mysql://localhost:3306/adventureworks",
#         driver="com.mysql.jdbc.Driver",
#         dbtable="transformed_table",
#         user="root",
#         password="ashiqur"
#     ).mode("overwrite").save()

# # Define tasks in the DAG
# extract_data = MySqlOperator(
#     task_id='extract_data_from_mysql',
#     mysql_conn_id='mysql_default',
#     sql="SELECT * FROM sales",
#     dag=dag
# )

# transform_data = PythonOperator(
#     task_id='transform_data_with_pyspark',
#     python_callable=perform_etl,
#     dag=dag
# )

# # Set task dependencies
# extract_data >> transform_data
