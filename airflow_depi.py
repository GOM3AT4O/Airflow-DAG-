from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import random

def welcome_message():
    print("Welcome Welcome! My name is gom3a")

def generate_random_number():
    num = random.randint(1, 100)
    with open("/tmp/random.txt", "w") as f:
        f.write(str(num))
    print(f"Random number {num} saved to /tmp/random.txt")


with DAG(
    dag_id="Airflow_Depi",
    start_date=datetime(2025, 10, 3),
    schedule_interval=timedelta(minutes=1),
    catchup=False
) as dag:

    task1 = BashOperator(
        task_id="print_date",
        bash_command="date"
    )

    task2 = PythonOperator(
        task_id="welcome_message",
        python_callable=welcome_message
    )


    task3 = PythonOperator(
        task_id="generate_random",
        python_callable=generate_random_number
    )

    task1 >> task2 >> task3
