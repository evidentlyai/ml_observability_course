---
description: What ML monitoring is, the challenges of production ML monitoring, and how it differs from ML observability.
---

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

![](<../../../images/2023109\_course\_module1\_fin\_images.024-min.png>)

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

![](<../../../images/2023109\_course\_module1\_fin\_images.030-min.png>)

## Who should care about ML monitoring and observability?

The short answer: everyone who cares about the model's impact on business. At the same time, different users might care about specific aspects of the ML model performance. For example:

* **Data scientists** might be interested in model performance and data drift metrics.
* **Data science managers** need to know whether it is time to retrain the model.
* **Product managers** want to understand model limitations.
* **Data engineers** want to ensure data quality and integrity.

Other stakeholders include model users, business stakeholders, support, and compliance teams.

![](<../../../images/2023109\_course\_module1\_fin\_images.031-min.png>)

## Summing up

Often used interchangeably, ML monitoring and ML observability are quite different. While ML monitoring helps detect issues, ML observability helps understand and analyze their root causes and proactively explore the model performance. In this course, we’ll cover both and refer to ML monitoring as the subset of ML observability. 

There are many use cases where ML monitoring and observability are crucial for the overall model's well-being, from detecting and resolving issues to understanding processes behind the model. ML monitoring might involve different stakeholders, from data scientists and ML engineers to business teams.
