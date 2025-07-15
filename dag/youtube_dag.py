from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import my_youtube_script  # your script as a module

default_args = {
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG('youtube_data_pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    fetch_store_task = PythonOperator(
        task_id='fetch_and_store',
        python_callable=my_youtube_script.fetch_and_store
    )
    
    fetch_store_task
