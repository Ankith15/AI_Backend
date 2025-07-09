from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Ankith',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='heart_disease_ml_pipeline',
    default_args=default_args,
    description='Automated heart disease pipeline using Spark and MLflow',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    spark_preprocess = BashOperator(
        task_id='spark_preprocessing',
        bash_command='python spark_preprocess.py',
        cwd='/opt/airflow/project'

    )

    train_model = BashOperator(
        task_id='train_model_with_mlflow',
        bash_command='python train_with_mlflow.py',
        cwd='/opt/airflow/smartheart'
    )

    spark_preprocess >> train_model
