import datetime

from sklearn import datasets

from evidently.report import Report
from evidently.metrics import ColumnDriftMetric, DatasetDriftMetric

from evidently.test_suite import TestSuite
from evidently.test_preset import DataDriftTestPreset

from evidently.ui.dashboards import CounterAgg
from evidently.ui.dashboards import DashboardPanelCounter
from evidently.ui.dashboards import DashboardPanelPlot
from evidently.ui.dashboards import PanelValue
from evidently.ui.dashboards import PlotType
from evidently.ui.dashboards import ReportFilter
from evidently.ui.dashboards import DashboardPanelTestSuite
from evidently.ui.dashboards import TestFilter
from evidently.ui.dashboards import TestSuitePanelType
from evidently.renderers.html_widgets import WidgetSize

from evidently.ui.workspace import Workspace
from evidently.ui.workspace import WorkspaceBase

bank_marketing = datasets.fetch_openml(name='bank-marketing', as_frame='auto')
bank_marketing_data = bank_marketing.frame

reference_data = bank_marketing_data[5000:7000]
prod_simulation_data = bank_marketing_data[7000:]
batch_size = 2000

WORKSPACE = "bank_data"

YOUR_PROJECT_NAME = "Bank Marketing Classification"
YOUR_PROJECT_DESCRIPTION = "Test project using Bank Marketing dataset"


def create_data_quality_report(i: int):
    report = Report(
        metrics=[
            DatasetDriftMetric(),
            ColumnDriftMetric(column_name="Class"),
        ],
        timestamp=datetime.datetime.now() + datetime.timedelta(days=i),
    )

    report.run(reference_data=reference_data, current_data=prod_simulation_data[i * batch_size : (i + 1) * batch_size])
    return report

def create_data_drift_test_suite(i: int):
    suite = TestSuite(
        tests=[
            DataDriftTestPreset()
        ],
        timestamp=datetime.datetime.now() + datetime.timedelta(days=i),
        tags = []
    )

    suite.run(reference_data=reference_data, current_data=prod_simulation_data[i * batch_size : (i + 1) * batch_size])
    return suite

def create_project(workspace: WorkspaceBase):
    project = workspace.create_project(YOUR_PROJECT_NAME)
    project.description = YOUR_PROJECT_DESCRIPTION
    project.dashboard.add_panel(
        DashboardPanelCounter(
            filter=ReportFilter(metadata_values={}, tag_values=[]),
            agg=CounterAgg.NONE,
            title="Bank Marketing Dataset",
        )
    )
    
    project.dashboard.add_panel(
        DashboardPanelPlot(
            title="Target Drift",
            filter=ReportFilter(metadata_values={}, tag_values=[]),
            values=[
                PanelValue(
                    metric_id="ColumnDriftMetric",
                    metric_args={"column_name.name": "Class"},
                    field_path=ColumnDriftMetric.fields.drift_score,
                    legend="target: Class",
                ),
            ],
            plot_type=PlotType.LINE,
            size=WidgetSize.HALF
        )
    )

    project.dashboard.add_panel(
        DashboardPanelPlot(
            title="Dataset Drift",
            filter=ReportFilter(metadata_values={}, tag_values=[]),
            values=[
                PanelValue(metric_id="DatasetDriftMetric", field_path="share_of_drifted_columns", legend="Drift Share"),
            ],
            plot_type=PlotType.BAR,
            size=WidgetSize.HALF
        )
    )

    project.dashboard.add_panel(
        DashboardPanelTestSuite(
            title="All tests",
            filter=ReportFilter(metadata_values={}, tag_values=[], include_test_suites=True),
            size=WidgetSize.HALF
        )
    )

    project.dashboard.add_panel(
        DashboardPanelTestSuite(
            title="All tests: detailed",
            filter=ReportFilter(metadata_values={}, tag_values=[], include_test_suites=True),
            size=WidgetSize.HALF,
            panel_type=TestSuitePanelType.DETAILED

        )
    )
    
    project.save()
    return project


def create_demo_project(workspace: str):
    ws = Workspace.create(workspace)
    project = create_project(ws)

    for i in range(0, 10):
        report = create_data_quality_report(i=i)
        ws.add_report(project.id, report)

        suite = create_data_drift_test_suite(i=i)
        ws.add_report(project.id, suite)


if __name__ == "__main__":
    create_demo_project(WORKSPACE)
