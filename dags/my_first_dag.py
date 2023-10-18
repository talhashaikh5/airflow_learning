from airflow import DAG
from datetime import datetime


with DAG(
    dag_id="my_first_dag"
    description="This is my first dag that i am playing with"
    start_date=datetime(2023,10,18)

) as dag:
    pass