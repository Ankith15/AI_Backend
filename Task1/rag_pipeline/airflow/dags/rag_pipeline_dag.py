from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'ankith',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='rag_pipeline_indexing',
    default_args=default_args,
    description='RAG PDF embedding and indexing pipeline',
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    build_index = BashOperator(
        task_id='build_faiss_index',
        bash_command='python index_pdf.py',
        cwd='/opt/airflow/rag_pipeline'

    )
