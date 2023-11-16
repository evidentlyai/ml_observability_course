import os
import pandas as pd 

from datetime import datetime, timedelta
from sklearn import datasets
import mlflow

from evidently.test_suite import TestSuite 
from evidently.test_preset import DataDriftTestPreset

bank_marketing = datasets.fetch_openml(name='bank-marketing', as_frame='auto')
bank_marketing_data = bank_marketing.frame
reference_data = bank_marketing_data[5000:7000]
prod_simulation_data = bank_marketing_data[7000:]
batch_size = 2000 

#set experiment
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Drift Tests")

for batch_id in range(10):
	with mlflow.start_run() as run:
		data_drift_suite = TestSuite(tests=[DataDriftTestPreset()])
		data_drift_suite.run(reference_data=reference_data,
			current_data=prod_simulation_data[batch_id * batch_size : (batch_id + 1) * batch_size])

		data_drift_suite.save_html("data_drift_suite.html")

		#Log parameters
		mlflow.log_param("batch_id", f"batch_{batch_id}")
		mlflow.log_param("success_tests", data_drift_suite.as_dict()['summary']['success_tests'])
		mlflow.log_param("failed_tests", data_drift_suite.as_dict()['summary']['failed_tests'])

		#Log report
		mlflow.log_artifact("data_drift_suite.html")

		print(run.info)