import datetime
import time
import logging 
import psycopg

import pandas as pd

from sklearn import datasets

from evidently.report import Report
from evidently.metrics import ColumnDriftMetric, DatasetDriftMetric

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")


create_table_statement = """
drop table if exists drift_metrics;
create table drift_metrics(
	timestamp timestamp,
	target_drift float,
	share_drifted_columns float
)
"""

bank_marketing = datasets.fetch_openml(name='bank-marketing', as_frame='auto')
bank_marketing_data = bank_marketing.frame

reference_data = bank_marketing_data[5000:5500]
prod_simulation_data = bank_marketing_data[7000:]
mini_batch_size = 50

def prep_db():
	with psycopg.connect("host=localhost port=5432 user=postgres password=example", autocommit=True) as conn:
		res = conn.execute("SELECT 1 FROM pg_database WHERE datname='test'")
		if len(res.fetchall()) == 0:
			conn.execute("create database test;")
		with psycopg.connect("host=localhost port=5432 dbname=test user=postgres password=example") as conn:
			conn.execute(create_table_statement)

def calculate_metrics_postgresql(curr, i):
	report = Report(
		metrics=[
			DatasetDriftMetric(),
			ColumnDriftMetric(column_name="Class"),
		])

	report.run(reference_data=reference_data, current_data=prod_simulation_data[i * mini_batch_size : (i + 1) * mini_batch_size])

	result = report.as_dict()

	target_drift = result['metrics'][1]['result']['drift_score']
	share_drifted_columns = result['metrics'][0]['result']['share_of_drifted_columns']

	curr.execute(
		"insert into drift_metrics(timestamp, target_drift, share_drifted_columns) values (%s, %s, %s)",
		(datetime.datetime.now(), target_drift, share_drifted_columns)
	)

def batch_monitoring_backfill():
	prep_db()
	with psycopg.connect("host=localhost port=5432 dbname=test user=postgres password=example", autocommit=True) as conn:
		for i in range(50):
			with conn.cursor() as curr:
				calculate_metrics_postgresql(curr, i)
			logging.info("data sent")
			time.sleep(3)


if __name__ == '__main__':
	batch_monitoring_backfill()
