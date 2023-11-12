---
description: Key considerations for ML monitoring setup. Service criticality, retraining cadence, reference dataset, and ML monitoring architecture.
---

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

![](<../../../images/2023109\_course\_module1\_fin\_images.050-min.png>)

## Model retraining cadence

ML monitoring and retraining are closely connected. Some retraining factors to keep in mind when setting up an ML monitoring system include:
* Frequency and costs of model retraining.
* How you implement the retraining: whether you want to monitor the metrics and retrain on a trigger or set up a predefined retraining schedule (for example, weekly).
* Issues that prevent updating the model too often, e.g., complex approval processes, regulations, need for manual testing.

![](<../../../images/2023109\_course\_module1\_fin\_images.052-min.png>)

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

For a deeper dive into the ML monitoring setup, head to [Module 4](../module-4-designing-effective-ml-monitoring/readme.md).
