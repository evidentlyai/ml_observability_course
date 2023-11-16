import os
import pandas as pd 

from datetime import datetime, timedelta
from sklearn import datasets

from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner

from evidently.test_suite import TestSuite 
from evidently.test_preset import DataDriftTestPreset, DataQualityTestPreset, DataStabilityTestPreset

dir_path = "reports"

@task(name="LOAD_DATA", retries=3, retry_delay_seconds=15)
def load_bank_data():
	bank_marketing = datasets.fetch_openml(name='bank-marketing', as_frame='auto')
	bank_marketing_data = bank_marketing.frame
	reference_data = bank_marketing_data[5000:7000]
	prod_simulation_data = bank_marketing_data[7000:]
	batch_size = 2000 
	return reference_data, prod_simulation_data[:batch_size]

@task(name="CHECK_QUALITY", retries=3, retry_delay_seconds=15)
def run_data_quality_test_suite(reference: pd.DataFrame, current: pd.DataFrame, ):
	data_quality_suite = TestSuite(tests=[DataQualityTestPreset()])
	data_quality_suite.run(reference_data=reference, current_data=current)
	if not data_quality_suite.as_dict()['summary']['all_passed']:
		try:
			os.mkdir(dir_path)
		except OSError:
			print("Creation of the directory {} failed".format(dir_path))
		data_quality_suite.save_html(os.path.join(dir_path, "data_quality_suite.html"))	

@task(name="CHECK_STABILITY", retries=3, retry_delay_seconds=15)
def run_data_stability_test_suite(reference: pd.DataFrame, current: pd.DataFrame):
	data_stability_suite = TestSuite(tests=[DataQualityTestPreset()])
	data_stability_suite.run(reference_data=reference, current_data=current)
	if not data_stability_suite.as_dict()['summary']['all_passed']:
		try:
			os.mkdir(dir_path)
		except OSError:
			print("Creation of the directory {} failed".format(dir_path))
		data_stability_suite.save_html(os.path.join(dir_path, "data_stability_suite.html"))	

@task(name="CHECK_DRIFT", retries=3, retry_delay_seconds=15)
def run_data_drift_test_suite(reference: pd.DataFrame, current: pd.DataFrame):
	data_drift_suite = TestSuite(tests=[DataDriftTestPreset()])
	data_drift_suite.run(reference_data=reference, current_data=current)
	if not data_drift_suite.as_dict()['summary']['all_passed']:
		try:
			os.mkdir(dir_path)
		except OSError:
			print("Creation of the directory {} failed".format(dir_path))
		data_drift_suite.save_html(os.path.join(dir_path, "data_drift_suite.html"))	

@flow(task_runner=SequentialTaskRunner)
def checks_flow():
	reference, current = load_bank_data()
	run_data_quality_test_suite(reference, current)
	run_data_stability_test_suite(reference, current)
	run_data_drift_test_suite(reference, current)

checks_flow()