# 1.5. ML monitoring architectures

{% embed url="https://www.youtube.com/watch?v=VVO6QFVbwTU&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=6" %}

**Video 5**. [ML monitoring architectures](https://www.youtube.com/watch?v=VVO6QFVbwTU&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=6), by Emeli Dral

It is essential to start monitoring ML models as soon as you deploy them to production. To do that, you also need to decide how exactly you implement the ML monitoring process. There are various ML monitoring architectures to choose from, both when it comes to the monitoring backend and frontend. 

## Monitoring backend

**Batch ML monitoring**. To set up a batch ML monitoring system, create a pipeline with metric calculations and schedule an ML monitoring job. You can run monitoring jobs periodically (e.g., every 10 seconds, hourly) or on a trigger (e.g., when a new batch of labeled data arrives). As some monitoring metrics like data drift are calculated in batch mode, this architecture works for both batch and online inference.

**Near real-time (streaming) ML monitoring**. In this case, you send data from the ML service to an ML monitoring system directly, calculate monitoring metrics on the fly, and visualize them on an online dashboard. This type of architecture is suited for ML models that require immediate or near-real-time monitoring.

**Ad hoc reporting** is a great alternative when your resources are limited. You can use Python scripts to calculate and analyze metrics in your notebook. This is a good first step in logging model performance and data quality.

![](<../../../images/2023109\_course\_module1\_fin\_images.061.png>)

## Monitoring frontend

When it comes to visualizing the results of monitoring, you also have options. 

**No user interface**. You can start with collecting the data without visualizing it. In this scenario, you can simply log metrics to a database. This allows you to implement alerting and historical data logging.

**One-off reports**. You can also generate reports as needed and create visualizations or specific one-off analyses based on the model logs. You can create your own reports in Python/R or use different BI visualization tools.

![](<../../../images/2023109\_course\_module1\_fin\_images.065.png>)

**BI Systems**. If you want to create a dashboard to track ML monitoring metrics over time, you can also reuse existing business intelligence or software monitoring systems. In this scenario, you must connect existing tools to the ML metric database and add panels or plots to the dashboard.

**Dedicated ML monitoring**. As a more sophisticated approach, you can set up a separate visualization system that gives you an overview of all your ML models and datasets and provides an ongoing, updated view of metrics.

![](<../../../images/2023109\_course\_module1\_fin\_images.066.png>)

## Summing up

Each ML monitoring architecture has its pros and cons. When choosing between them, consider existing tools, the scale of ML deployments, and available team resources for systems support. Be pragmatic: you can start with a simpler architecture and expand later. 

For a deeper dive into the ML monitoring architectures with specific code examples, head to [Module 5](ml-observability-course/module-5-ml-pipelines-validation-and-testing.md) and [Module 6](ml-observability-course/module-6-deploying-an-ml-monitoring-dashboard.md). 
