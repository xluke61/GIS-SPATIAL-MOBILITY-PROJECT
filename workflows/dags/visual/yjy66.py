from airflow import DAG
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from airflow.models.param import Param
from sagemaker_studio import Project
from workflows.airflow.providers.amazon.aws.operators.sagemaker_workflows import NotebookOperator

project = Project()

with DAG(
    dag_id='yjy66',
    description='',default_args={},
    schedule=None,
    is_paused_upon_creation=False,
    tags=[],
    catchup=False,
) as dag:

    SageMakerNotebookOperator_1770936498473 = NotebookOperator(
        task_id='notebook-task',
        input_config={
            "input_path": 'getting_started.ipynb',
            "input_params": {}
        },
        output_config={"output_formats": ['NOTEBOOK']},
        poll_interval=5,
    )