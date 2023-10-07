---
description: Introduction to ML monitoring and observability.
---

# Module 1. Introduction

This theoretical module introduces the key topics of machine learning monitoring and observability.

It covers the following topics:
* what can go wrong with ML models in production;
* what ML monitoring and observability are and how they fit in the ML lifecycle;
* what types of evaluation you might need, from model quality to data drift;
* key considerations to keep in mind when designing your monitoring. 

At the end of this module, you will know the key concepts related to ML monitoring and observability and how they will be covered throughout the course.

# 1.1. ML lifecycle. What can go wrong with ML in production?

{% embed url="https://www.youtube.com/watch?v=8I89FY2eelM&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=2" %}

**Video 1**. [ML lifecycle. What can go wrong with ML in production](https://www.youtube.com/watch?v=8I89FY2eelM&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=2), by Emeli Dral

## Evaluations in ML model lifecycle

Building a successful ML model involves the following stages:
* Data preparation,
* Feature engineering,
* Model training,
* Model evaluation,
* Model deployment.

You can perform different types of evaluations at each of these stages. For example,
* During data preparation, exploratory data analysis (EDA) helps to understand the dataset and validate the problem statement.
* At the experiment stage, performing cross-validation and holdout testing helps validate and test if ML models are useful.

However, the work does not stop here! Once the best model is deployed to production and starts bringing business value, every erroneous prediction has its costs. It is crucial to ensure that this model functions stably and reliably. To do that, one must continuously monitor the production ML model and data.

## What can go wrong in production?

Many things can go wrong once you deploy an ML model to the real world. Here are some examples.

**Training-serving skew**. Model degrades if training data is very different from production data.

**Data quality issues**. In most cases, when something is wrong with the model, this is due to data quality and integrity issues. These can be caused by:
* Data processing issues, e.g., broken pipelines or infrastructure updates.
* Data schema changes in the upstream system, third-party APIs, or catalogs.
* Data loss at source when dealing with broken sensors, logging errors, database outages, etc.

**Broken upstream model**. Often, not one model but a chain of ML models operates in production. If one model gives wrong outputs, it can affect downstream models.

**Concept drift**. Gradual concept drift occurs when the target function continuously changes over time, leading to model degradation. If the change is sudden – like the recent pandemic – you’re dealing with sudden concept drift. 

**Data drift**. Distribution changes in the input features may signal data drift and potentially cause ML model performance degradation. For example, a significant number of users coming from a new acquisition channel can negatively affect the model trained on user data. Chances are that users from different channels behave differently. To get back on track, the model needs to learn new patterns. 

**Underperforming segments**. A model might perform differently on diverse data segments. It is crucial to monitor performance across all segments.

**Adversarial adaptation**. In the era of neural networks, models might face adversarial attacks. Monitoring helps detect these issues on time.

## Summing up

Many factors can impact the performance of an ML model in production. ML monitoring and observability are crucial to ensure that models perform as expected and provide value.

# 1.2. What is ML monitoring and observability?

{% embed url="https://www.youtube.com/watch?v=Wfphz6TUikM&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=3" %}

**Video 2**. [What is ML monitoring and observability](https://www.youtube.com/watch?v=Wfphz6TUikM&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=3), by Emeli Dral

## What is ML monitoring?

**Machine learning model monitoring** is a series of techniques to track and analyze the performance of ML models in production. It helps measure ongoing model quality, detect potential issues, and resolve them on time.

## When to monitor?

There are three main scenarios when you need ML model monitoring:
* **Models in production**. Upon deploying ML models to production, you need to keep tabs on the ongoing performance and business impact.
* **Models in shadow deployment**. In shadow mode, you track the behavior of a candidate model when predictions are generated but not acted upon (in other words, ML models generate outputs, but these outputs are not used in downstream systems).
* **During A/B testing**. In this case, you track and compare the results of active candidate models.

## Challenges of ML monitoring

**It’s not just software performance**. Software monitoring has been around for ages. If a software service is running in production, you need to monitor service health metrics such as uptime, memory usage, and latency. This also applies to ML monitoring.  

**However, ML monitoring also introduces two extra layers to keep tabs on**:
* Data health,
* Model health.

Accordingly, you also need to track data quality and model performance metrics.

**Selecting the right metric and threshold can be a challenging task**. It is always case-specific. Let’s take a binary classification problem as an example:
* For balanced datasets, an accuracy score of 99% means that the model performs pretty well.
* However, for unbalanced datasets (e.g., in fraud detection tasks), the same accuracy score does not allow making meaningful conclusions about the model quality.

**Ground truth is not available immediately** to calculate ML model performance metrics. In this case, you can use proxy metrics like data quality to monitor for early warning signs. 

## ML monitoring vs ML observability

Often used interchangeably, ML monitoring and ML observability are quite different.

**ML monitoring**:
* tracks a pre-defined set of metrics,
* helps detect issues (“What happened?”, “Is the system working?”),
* is more reactive (helps to find “known unknowns”).

**ML observability**:
* gives visibility into the system behavior,
* helps understand and analyze root causes (“Why it happened? Where exactly?”),
* is more proactive (helps to find “unknown unknowns”).

In this course, we refer to ML monitoring as the subset of ML observability. 

## Why ML monitoring and observability matter

ML monitoring and observability help:

* **Detect issues** and alert about missing data, features out of expected range, data drift, or sudden model quality drops.
* **Find a root cause** by locating corrupted data, detecting low-performing segments, helping select the right data to label, etc.
* **Understand ML model behavior**. It provides insights into how users interact with the model or whether there are changes in the environment where the model functions.
* **Trigger actions**. Based on the calculated data and model health metrics, you can trigger fallback, model switching, or automatic retraining.
* **Document ML model performance** to provide information to the stakeholders.

## Who should care about ML monitoring and observability?

The short answer: everyone who cares about the model's impact on business. At the same time, different users might care about specific aspects of the ML model performance. For example:

* **Data scientists** might be interested in model performance and data drift metrics.
* **Data science managers** need to know whether it is time to retrain the model.
* **Product managers** want to understand model limitations.
* **Data engineers** want to ensure data quality and integrity.

Other stakeholders include model users, business stakeholders, support, and compliance teams.

## Summing up

Often used interchangeably, ML monitoring and ML observability are quite different. While ML monitoring helps detect issues, ML observability helps understand and analyze their root causes and proactively explore the model performance. In this course, we’ll cover both and refer to ML monitoring as the subset of ML observability. 

There are many use cases where ML monitoring and observability are crucial for the overall model's well-being, from detecting and resolving issues to understanding processes behind the model. ML monitoring might involve different stakeholders, from data scientists and ML engineers to business teams.

# 1.3. ML monitoring metrics. What exactly can you monitor?

{% embed url="https://www.youtube.com/watch?v=DCFvZvpDks0&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=4" %}

**Video 3**. [ML monitoring metrics](https://www.youtube.com/watch?v=DCFvZvpDks0&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=4), by Emeli Dral

An ML-based service is more than just an ML model. One needs to keep tabs on all the facets of the ML system quality. When it comes to monitoring the system performance, there are different groups of metrics.

## Software system health

It doesn’t matter how excellent your model is when the whole ML system is down. To track the overall system health, you can reuse existing monitoring schemes from other production services. Standard software performance metrics include latency, error rate, memory usage, disk usage, etc. 

## Data quality and data integrity

In many cases, model issues stem from issues with the input data. To monitor data quality and integrity, you can keep tabs on metrics like the share of missing values, type mismatch, or range violations for important features. The goal here is to ensure the stability of data pipelines. 

## ML model quality and relevance

ML model performance metrics help to ensure that ML models work as expected:
* Standard metrics help evaluate the quality of the ML model in production. For example, you can track metrics like precision and recall for classification, MAE or RMSE for regression, or top-k accuracy for ranking.
* You can also track use-case specific quality metrics like bias or fairness: for example, through metrics like predictive parity or equalized odds.
* When ground truth is unavailable or delayed, use proxy metrics. Keep tabs on prediction drift, input data drift, or share of new categories. These metrics can signal potential problems before the ML model quality is affected. 

## Business KPIs

The ultimate measure of the model quality is its impact on the business. Depending on business needs, you may want to monitor clicks, purchases, loan approval rates, cost savings, etc. This is typically custom to the use case and might involve collaborating with product managers or business teams to determine the right business KPIs. 

For a deeper dive into **ML model quality and relevance** and **data quality and integrity** metrics, head to [Module 2](ml-observability-course/module-2-ml-monitoring-metrics.md).

# 1.4. Key considerations for ML monitoring setup

{% embed url="https://www.youtube.com/watch?v=LnfL9Nu0tm4&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=5" %}

**Video 4**. [Key considerations for ML monitoring setup](https://www.youtube.com/watch?v=LnfL9Nu0tm4&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=5), by Emeli Dral

When designing the ML monitoring setup for a specific model, you might want to consider the following aspects:
* Matching the ML monitoring setup to the use case
* Model retraining cadence
* Choice of reference dataset
* Custom metrics 

## Matching ML monitoring setup and the use case

While setting up an ML monitoring system, it makes sense to align the complexity of monitoring with the complexity of the deployment and operations of the ML service. Some factors to consider:
* **ML service implementation**. Is it a real-time production service, batch Airflow DAG, or an ad hoc Python script?
* **Feedback loop and environmental stability**. Both influence the cadence of metrics calculations and the choice of specific metrics.
* **Service criticality**. What is the business cost of model quality drops? What risks should we monitor for? More critical models might require a more complex monitoring setup.

## Model retraining cadence

ML monitoring and retraining are closely connected. Some retraining factors to keep in mind when setting up an ML monitoring system include:
* Frequency and costs of model retraining.
* How you implement the retraining: whether you want to monitor the metrics and retrain on a trigger or set up a predefined retraining schedule (for example, weekly).
* Issues that prevent updating the model too often, e.g., complex approval processes, regulations, need for manual testing.

## Reference dataset

In a situation where various production models use different data types – e.g., numerical and categorical features, tabular data, text data, images, or videos – setting up data quality monitoring can be overwhelming. 

Instead, you can use a **reference dataset** to help automatically generate different tests based on the provided example and compare the new batches of data against it. 

If you follow this strategy, it is important that you select and curate an appropriate reference: as it becomes as important as choosing the right metrics. A “good” reference dataset must represent the expected data patterns correctly.

You can also utilize a reference dataset as a baseline for the distribution drift comparison. You can consider having a fixed reference dataset, a moving one, or multiple windows. 

Based on the scenario, you can use different reference datasets: for example, one dataset for distribution drift detection and another to generate data quality test conditions.

## Custom metrics

Standard monitoring metrics like accuracy or AUC are good starting points. However, depending on the use case, you may need to introduce more comprehensive custom monitoring metrics. 

Some examples of custom metrics include:
* **Use-case specific model quality metrics** (e.g., lift-10% for churn prediction in the telecom industry),
* **Heuristics** that reflect quality (e.g., the share of predictions higher than a specific threshold), especially when ground truth is not available.
* **Business quality metrics** and KPIs (e.g., estimated savings),
* **Custom drift detection methods** beyond standard statistical tests.

## Summing up

While designing an ML monitoring system, tailor your approach to fit your specific requirements and challenges:
* Ensure the monitoring setup aligns with the complexity of your use case.
* Consider binding retraining to monitoring, if relevant.
* Use reference datasets to simplify the monitoring process but make sure they are carefully curated.
* Define custom metrics that fit your problem statement and data properties.

For a deeper dive into the ML monitoring setup, head to [Module 4](ml-observability-course/module-4-designing-effective-ml-monitoring.md).

# 1.5. ML monitoring architectures

{% embed url="https://www.youtube.com/watch?v=VVO6QFVbwTU&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=6" %}

**Video 5**. [ML monitoring architectures](https://www.youtube.com/watch?v=VVO6QFVbwTU&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=6), by Emeli Dral

It is essential to start monitoring ML models as soon as you deploy them to production. To do that, you also need to decide how exactly you implement the ML monitoring process. There are various ML monitoring architectures to choose from, both when it comes to the monitoring backend and frontend. 

## Monitoring backend

**Batch ML monitoring**. To set up a batch ML monitoring system, create a pipeline with metric calculations and schedule an ML monitoring job. You can run monitoring jobs periodically (e.g., every 10 seconds, hourly) or on a trigger (e.g., when a new batch of labeled data arrives). As some monitoring metrics like data drift are calculated in batch mode, this architecture works for both batch and online inference.

**Near real-time (streaming) ML monitoring**. In this case, you send data from the ML service to an ML monitoring system directly, calculate monitoring metrics on the fly, and visualize them on an online dashboard. This type of architecture is suited for ML models that require immediate or near-real-time monitoring.

**Ad hoc reporting** is a great alternative when your resources are limited. You can use Python scripts to calculate and analyze metrics in your notebook. This is a good first step in logging model performance and data quality.

## Monitoring frontend

When it comes to visualizing the results of monitoring, you also have options. 

**No user interface**. You can start with collecting the data without visualizing it. In this scenario, you can simply log metrics to a database. This allows you to implement alerting and historical data logging.

**One-off reports**. You can also generate reports as needed and create visualizations or specific one-off analyses based on the model logs. You can create your own reports in Python/R or use different BI visualization tools.

**BI Systems**. If you want to create a dashboard to track ML monitoring metrics over time, you can also reuse existing business intelligence or software monitoring systems. In this scenario, you must connect existing tools to the ML metric database and add panels or plots to the dashboard.

**Dedicated ML monitoring**. As a more sophisticated approach, you can set up a separate visualization system that gives you an overview of all your ML models and datasets and provides an ongoing, updated view of metrics.

## Summing up

Each ML monitoring architecture has its pros and cons. When choosing between them, consider existing tools, the scale of ML deployments, and available team resources for systems support. Be pragmatic: you can start with a simpler architecture and expand later. 

For a deeper dive into the ML monitoring architectures with specific code examples, head to [Module 5](ml-observability-course/module-5-ml-pipelines-validation-and-testing.md) and [Module 6](ml-observability-course/module-6-deploying-an-ml-monitoring-dashboard.md). 
