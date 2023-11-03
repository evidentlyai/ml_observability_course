import os
import pandas as pd

from datetime import datetime
from datetime import timedelta
from sklearn import datasets

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from evidently.test_suite import TestSuite
from evidently.test_preset import DataDriftTestPreset


default_args = {
    "start_date": datetime(2023, 1, 1),
    "owner": "emeli",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dir_path = "reports"
file_path = "data_drift_suite.html"

def load_data_execute(**context):
    bank_marketing= datasets.fetch_openml(name='bank-marketing', as_frame='auto')
    bank_marketing_data = bank_marketing.frame
    context["ti"].xcom_push(key="data_frame", value=bank_marketing_data)


def drift_analysis_execute(**context):
    data = context.get("ti").xcom_pull(key="data_frame")

    reference_data = data[5000: 7000]
    prod_simulation_data = data[7000:]
    batch_size = 2000

    data_drift_suite = TestSuite(tests=[DataDriftTestPreset()])
    data_drift_suite.run(reference_data=reference_data, current_data=prod_simulation_data[:batch_size])

    if not data_drift_suite.as_dict()['summary']['all_passed']:
        return "create_report"


def create_report_execute(**context):
    data = context.get("ti").xcom_pull(key="data_frame")
    
    reference_data = data[5000: 7000]
    prod_simulation_data = data[7000:]
    batch_size = 2000

    data_drift_suite = TestSuite(tests=[DataDriftTestPreset()])
    data_drift_suite.run(reference_data=reference_data, current_data=prod_simulation_data[:batch_size])

    try:
        os.mkdir(dir_path)
    except OSError:
        print("Creation of the directory {} failed".format(dir_path))
    data_drift_suite.save_html(os.path.join(dir_path, file_path))


with DAG(
    dag_id="evidently_conditional_drift",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
) as dag:

    load_data = PythonOperator(
        task_id="load_data",
        python_callable=load_data_execute,
        provide_context=True
    )

    drift_analysis = PythonOperator(
        task_id="drift_analysis",
        python_callable=drift_analysis_execute,
        provide_context=True,
    )

    create_report = PythonOperator(
        task_id="create_report",
        provide_context=True,
        python_callable=create_report_execute,
    )


load_data >> drift_analysis >> [create_report]