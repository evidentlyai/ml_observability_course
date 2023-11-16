---
description: A brief summary of the Open-source ML observability course learnings.
---

# 6.5. Connecting the dots: full-stack ML observability

{% embed url="https://youtu.be/lK3OE473W0I?si=sPBZF_7wtUYgtRVO" %}

**Video 5**. [Connecting the dots: full-stack ML observability](https://youtu.be/lK3OE473W0I?si=sPBZF_7wtUYgtRVO), by Emeli Dral

## What we covered in the course

This is the final lesson of the Open-source ML observability course. Let’s recap what we’ve learned during the course!

**ML monitoring metrics**
We covered what metrics to use to assess [data quality](https://learn.evidentlyai.com/ml-observability-course/module-2-ml-monitoring-metrics/data-quality-in-ml), [model quality](https://learn.evidentlyai.com/ml-observability-course/module-2-ml-monitoring-metrics/ml-quality-metrics-classification-regression-ranking), and [data drift](https://learn.evidentlyai.com/ml-observability-course/module-2-ml-monitoring-metrics/data-prediction-drift-in-ml). We also discussed how to implement [custom metrics](https://learn.evidentlyai.com/ml-observability-course/module-4-designing-effective-ml-monitoring/custom-metrics-ml-monitoring) for specific use cases. For example, you can integrate custom metrics related to business KPIs and specific aspects of model quality into ML monitoring.

**ML monitoring design**
We covered different aspects of ML monitoring design, including how to select and use [reference datasets](https://learn.evidentlyai.com/ml-observability-course/module-4-designing-effective-ml-monitoring/how-to-choose-reference-dataset-ml-monitoring). We also discussed the connection between [model retraining](https://learn.evidentlyai.com/ml-observability-course/module-4-designing-effective-ml-monitoring/when-to-retrain-ml-models) cadence and ML monitoring.

**ML monitoring architectures**
We explored different [ML monitoring architectures](https://learn.evidentlyai.com/ml-observability-course/module-4-designing-effective-ml-monitoring/choosing-ml-monitoring-deployment-architecture), from ad hoc reports and test suites to batch and real-time ML monitoring, and learned how to implement them in practice in [Module 5](https://learn.evidentlyai.com/ml-observability-course/module-5-ml-pipelines-validation-and-testing) and [Module 6](https://learn.evidentlyai.com/ml-observability-course/module-6-deploying-an-ml-monitoring-dashboard).

**ML monitoring for unstructured data**
We also touched on how to build a monitoring system for [text data](https://learn.evidentlyai.com/ml-observability-course/module-3-ml-monitoring-for-unstructured-data/monitoring-data-drift-on-raw-text-data) and [embeddings](https://learn.evidentlyai.com/ml-observability-course/module-3-ml-monitoring-for-unstructured-data/monitoring-embeddings-drift).

![](<../../../images/202310\_module6.022-min.png>)

## Summing up

**Start small and expand.** Ad hoc reports are a good starting point for ML monitoring that is easy to implement. It is useful for initial learning about data and model quality before establishing a comprehensive monitoring system. Don’t hesitate to start small! 

As you progress and deploy multiple models in production, or if you work with mission-critical use cases, you’d need a more extensive setup.

**Jobs to be done** to implement full-stack production ML observability:
* **Immediate monitoring flow** helps to detect issues and to alert during model inference. If you have a production-critical service, it is essential to implement it. 
* **Delayed monitoring flow** allows you to evaluate model quality when you get the labels (as ground truth is often not available immediately!).
* **Model evaluation flow** is needed to test model quality at updates and retraining.

**Observability components** to keep in mind when building ML monitoring:
* **Logging layer**. If you have a production service, implementing logging is a must to capture model inferences and collect performance metrics.
* **Alerting layer** allows you to monitor metrics and get notifications when things go wrong.
* **Dashboarding and analytics** help to visualize the performance, quickly detect root cause issues, and define actions for debugging and retraining.

## Enjoyed the course?

⭐️ **[Star Evidently on GitHub](https://github.com/evidentlyai/evidently)** to contribute back! This helps us create free, open-source tools and content for the community. 

📌 **Share your feedback** so we can make this course better. 

💻 **[Join our Discord community](https://discord.com/invite/xZjKRaNp8b)** for more discussions and materials on ML monitoring and observability. 
