# 4.7. How to choose the ML monitoring deployment architecture

{% embed url="https://youtu.be/Q1NUCDZFRbU?si=26GhKBdhFAIzxBgi" %}

**Video 7**. [How to choose the ML monitoring deployment architecture](https://youtu.be/Q1NUCDZFRbU?si=26GhKBdhFAIzxBgi), by Emeli Dral

There are alternative backends for machine learning monitoring architecture.

![](<../../../images/2023110\_course\_module4\_fin.086-min.png>)

## Ad-hoc reporting 

**Ad-hoc reporting** is a viable option when you've recently deployed a machine learning system, and do not have alternative monitoring systems. 
* It has **low engineering overhead**: you can use familiar tools like Jupyter notebooks, Python scripts, or R scripts. 
* It is **suitable for initial exploration** of data and model quality and shaping expectations about model performance, but is not a long-term monitoring solution.

![](<../../../images/2023110\_course\_module4\_fin.087-min.png>)

## Batch monitoring

**Batch ML monitoring** is a reliable and stable approach. It is suitable for both machine learning pipelines and services.

To implement batch monitoring, you need a workflow orchestration tool like Airflow or Kubeflow, and tools for calculating metrics and tests, such as Evidently.

**Pros**:
* Works well for both ML models implemented as batch pipelines and ML services.
* It is fairly simple to run monitoring jobs, especially if you already have a workflow orchestrator in place.
* You can use the same tools you use to run model training jobs during the experimental and validation phases of a machine learning lifecycle.
* You can combine immediate monitoring (e.g., data quality checks) and metrics dependent on ground truth (trigger-based calculations).

**Cons**:
* It is not real-time. There are some delays in metric computation due to additional resources required for running the infrastructure. 
* It might be complex if you don't have an existing orchestrator; setting up one can be resource-intensive.

![](<../../../images/2023110\_course\_module4\_fin.088-min.png>)

## Near real-time (streaming) monitoring

**Near real-time ML monitoring** architecture is suitable when you serve models as APIs and want to detect issues close to real-time. In this case, you push data from the machine learning service to the monitoring system.

You will need optimal storage solutions for time series data like Prometheus or Clickhouse, and tools like Grafana or Evidently for dashboarding and alerting.

**Pros**:
* Works for models deployed as an ML service as opposed to batch jobs.
* Suitable for scenarios when you need an immediate reaction to issues like missing data or outliers.

**Cons**: 
* High operational costs. Make sure you have the resources to maintain an additional monitoring service. 
* Potentially double effort. You will often still need to deal with delayed ground truth feedback and run batch monitoring jobs to calculate these metrics.

![](<../../../images/2023110\_course\_module4\_fin.089-min.png>)

**Custom monitoring backend**. You can also combine near real-time and batch monitoring. 

For example, you can combine:
* **Real-time checks**. You can send the data available at serving time directly from the ML service to an ML monitoring system to run input and model output checks and to generate alerts. 
* **Monitoring jobs**. For delayed ground truth or more complex checks, you can run monitoring jobs over prediction logs on a trigger or a schedule. 
* **Dashboarding tool**. You can log all results to the same metric storage system and get a single dashboard with panels for batch and real-time checks.

![](<../../../images/2023110\_course\_module4\_fin.090-min.png>)

## A case for batch ML monitoring 

Let’s go through the possible logic of choosing the ML monitoring architecture. 

First, let’s contrast it to **traditional software health monitoring**. You can typically implement additional service endpoints for metrics. Then, you can use tools like Prometheus to pull the metrics from these endpoints and store high-frequency time series data. You can add alerting and dashboard tools that rely on these metrics as a data source.

![](<../../../images/2023110\_course\_module4\_fin.092-min.png>)

However, integrating ML metrics into this same setup isn't as simple. Here is why:
* **Complex metrics**. Software metrics are usually more straightforward in terms of computation. You can run simple aggregations over data points like response times and memory usage. Some ML-related metrics (like the number of rows or missing values) are similar. But others, like model quality or statistical tests, involve more complex calculations.
* **Delayed feedback**. Model quality metrics like precision, recall or accuracy typically depend on delayed data. You cannot compute them at serving time and must wait for the labels. Once you calculate them, you must “backfill” time series data for the past period, since the moment you compute metrics is not the moment they refer to.
* **Reference dataset**. For checks like data and prediction drift, you must also pass a batch of data you are comparing against. This does not easily fit into traditional software architecture. 

ML model monitoring may require additional components:
* **Metric calculation pipelines**. If you run metric computation as jobs, you can use the appropriate backend for complex evaluations, for example, not just a SQL-like query. You can run complex evaluations like statistical drift and behavioral tests.
* **Run several different pipelines**. You can split metrics into separate pipelines. Some will run on a schedule (for metrics you can compute immediately) and others will be triggered by events like receiving new labeled data.
* **Passing the reference data**. You can implement complex pipelines that would involve querying the reference data, loading it, and comparing it against the current data batch. 

**Example**: you can cover the whole model lifecycle with batch checks and monitoring jobs.

![](<../../../images/2023110\_course\_module4\_fin.102-min.png>)

You can still combine this approach with traditional software monitoring system architecture. Once you implement a different metric computation backend for ML metrics, you can store the results in a metric storage and use it as a data source for your dashboarding system to visualize machine learning-related metrics.

![](<../../../images/2023110\_course\_module4\_fin.103-min.png>)

You can add a few ML-related metrics to an existing dashboard or create a separate ML monitoring dashboard.

## Summing up

We discussed the differences between different ML monitoring architectures. Here are some takeaways:
* Choose the ML architecture that matches your available resources, risk mitigation needs, and the complexity of your machine learning model.
* Even if you deploy a model as a service, consider batch ML monitoring. It is a more lightweight option, especially if you have a workflow orchestrator in place. It can handle complex evaluation scenarios.

## Enjoyed the content?

Star Evidently on GitHub to contribute back! This helps us create free, open-source tools and content for the community.
⭐️ [Star](https://github.com/evidentlyai/evidently) on GitHub!
