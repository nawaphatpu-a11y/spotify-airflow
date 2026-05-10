from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.insert(0, '/opt/airflow')
from etl_spotify import extract, validate, transform, load

with DAG(
    dag_id = "spotify_pipeline",
    start_date=datetime(2024,1,1),
    schedule="@daily",
    catchup=False
) as dag:

    task_extract = PythonOperator(
        task_id = "extract",
        python_callable = extract
    )

    task_validate = PythonOperator(
        task_id = "validate",
        python_callable = validate
    )

    task_transform = PythonOperator(
        task_id = "transform",
        python_callable = transform
    )

    task_load = PythonOperator(
        task_id = "load",
        python_callable = load
    )

    task_extract >> task_validate >> task_transform >> task_load
