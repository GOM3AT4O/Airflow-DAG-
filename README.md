📌 Overview

This project includes an Airflow DAG named Airflow_Depi with 3 tasks:

Print current date (BashOperator)

Print welcome message (PythonOperator)

Generate a random number and save to /tmp/random.txt (PythonOperator)

Task order: date → welcome → random

🚀 How to Run

Place DAG
Put airflow_depi.py inside your dags/ folder.

Start Airflow

docker-compose up -d


Access UI
Open http://localhost:8080

(default user/pass: airflow / airflow).

Enable & Trigger DAG

Turn on Airflow_Depi

Trigger a run

View logs in Graph View → Task → Log
