import datetime
import os.path
import time
import pandas as pd

from requests.exceptions import RequestException
from sklearn import datasets

from evidently.collector.client import CollectorClient
from evidently.collector.config import CollectorConfig, IntervalTrigger, ReportConfig

from evidently.test_suite import TestSuite
from evidently.test_preset import DataDriftTestPreset

from evidently.ui.dashboards import DashboardPanelTestSuite 
from evidently.ui.dashboards import ReportFilter
from evidently.ui.dashboards import TestFilter
from evidently.ui.dashboards import TestSuitePanelType
from evidently.renderers.html_widgets import WidgetSize
from evidently.ui.workspace import Workspace

COLLECTOR_ID = "default"
COLLECTOR_TEST_ID = "default_test"

PROJECT_NAME = "Bank Marketing: online service "

WORKSACE_PATH = "bank_data"

client = CollectorClient("http://localhost:8001")

bank_marketing = datasets.fetch_openml(name='bank-marketing', as_frame='auto')
bank_marketing_data = bank_marketing.frame

reference_data = bank_marketing_data[5000:5500]
prod_simulation_data = bank_marketing_data[7000:]
mini_batch_size = 50

def setup_test_suite():
    suite = TestSuite(tests=[
        DataDriftTestPreset(),
        ], 
        tags=[])

    suite.run(reference_data=reference_data, current_data=prod_simulation_data[:mini_batch_size])
    return ReportConfig.from_test_suite(suite)

def setup_workspace():
    ws = Workspace.create(WORKSACE_PATH)
    project = ws.create_project(PROJECT_NAME)
    project.dashboard.add_panel(
        DashboardPanelTestSuite(
            title="Data Drift tests",
            filter=ReportFilter(metadata_values={}, tag_values=[], include_test_suites=True),
            size=WidgetSize.HALF
        )
    )

    project.dashboard.add_panel(
        DashboardPanelTestSuite(
            title="Data Drift: detailed",
            filter=ReportFilter(metadata_values={}, tag_values=[], include_test_suites=True),
            size=WidgetSize.HALF,
            panel_type=TestSuitePanelType.DETAILED

        )
    )
    project.save()


def setup_config():
    ws = Workspace.create(WORKSACE_PATH)
    project = ws.search_project(PROJECT_NAME)[0]

    test_conf = CollectorConfig(trigger=IntervalTrigger(interval=5), report_config=setup_test_suite(), project_id=str(project.id))
    client.create_collector(COLLECTOR_TEST_ID, test_conf)

    client.set_reference(COLLECTOR_TEST_ID, reference_data)


def send_data():
    print("Start sending data")
    for i in range(50):
        try:
            data = prod_simulation_data[i * mini_batch_size : (i + 1) * mini_batch_size]
            client.send_data(COLLECTOR_TEST_ID, data)
            print("sent")
        except RequestException as e:
            print(f"collector service not available: {e.__class__.__name__}")
        time.sleep(1)


def main():
    if not os.path.exists(WORKSACE_PATH) or len(Workspace.create(WORKSACE_PATH).search_project(PROJECT_NAME)) == 0:
        setup_workspace()

    setup_config()

    send_data()


if __name__ == '__main__':
    main()