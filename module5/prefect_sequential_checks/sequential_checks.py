import os

import pandas as pd
from evidently.test_preset import (DataDriftTestPreset, DataQualityTestPreset,
                                   DataStabilityTestPreset)
from evidently.test_preset.test_preset import TestPreset
from evidently.test_suite import TestSuite
from sklearn import datasets

from prefect import flow, task

dir_path = "reports"


@task(name="LOAD_DATA", retries=3, retry_delay_seconds=15)
def load_bank_data():
    bank_marketing = datasets.fetch_openml(name="bank-marketing", as_frame="auto")
    bank_marketing_data = bank_marketing.frame
    reference_data = bank_marketing_data[5000:7000]
    prod_simulation_data = bank_marketing_data[7000:]
    batch_size = 2000
    return reference_data, prod_simulation_data[:batch_size]


@task(task_run_name="Run_{test_preset.__name__}", retries=3, retry_delay_seconds=15)
def run_test_suite(
    reference: pd.DataFrame, current: pd.DataFrame, test_preset: TestPreset
):
    test_suite = TestSuite(tests=[test_preset()])
    test_suite.run(reference_data=reference, current_data=current)
    if not test_suite.as_dict()["summary"]["all_passed"]:
        try:
            os.mkdir(dir_path)
        except OSError:
            print(f"Creation of the directory {dir_path} failed")
        test_suite.save_html(os.path.join(dir_path, f"{test_preset.__name__[:-10]}Report.html"))


@flow()
def checks_flow():
    reference, current = load_bank_data()
    run_test_suite(reference, current, DataDriftTestPreset)
    run_test_suite(reference, current, DataQualityTestPreset)
    run_test_suite(reference, current, DataStabilityTestPreset)


checks_flow()
