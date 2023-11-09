---
description: What can go wrong with data and machine learning services in production. Data quality issues, data drift, and concept drift.
---

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

![](<../../../images/2023109\_course\_module1\_fin\_images.005-min.png>)

However, the work does not stop here! Once the best model is deployed to production and starts bringing business value, every erroneous prediction has its costs. It is crucial to ensure that this model functions stably and reliably. To do that, one must continuously monitor the production ML model and data.

![](<../../../images/2023109\_course\_module1\_fin\_images.008-min.png>)

## What can go wrong in production?

Many things can go wrong once you deploy an ML model to the real world. Here are some examples.

**Training-serving skew**. Model degrades if training data is very different from production data.

**Data quality issues**. In most cases, when something is wrong with the model, this is due to data quality and integrity issues. These can be caused by:
* Data processing issues, e.g., broken pipelines or infrastructure updates.
* Data schema changes in the upstream system, third-party APIs, or catalogs.
* Data loss at source when dealing with broken sensors, logging errors, database outages, etc.

![](<../../../images/2023109\_course\_module1\_fin\_images.011-min.png>)

**Broken upstream model**. Often, not one model but a chain of ML models operates in production. If one model gives wrong outputs, it can affect downstream models.

![](<../../../images/2023109\_course\_module1\_fin\_images.012-min.png>)

**Concept drift**. Gradual concept drift occurs when the target function continuously changes over time, leading to model degradation. If the change is sudden – like the recent pandemic – you’re dealing with sudden concept drift. 

**Data drift**. Distribution changes in the input features may signal data drift and potentially cause ML model performance degradation. For example, a significant number of users coming from a new acquisition channel can negatively affect the model trained on user data. Chances are that users from different channels behave differently. To get back on track, the model needs to learn new patterns. 

![](<../../../images/2023109\_course\_module1\_fin\_images.015-min.png>)

**Underperforming segments**. A model might perform differently on diverse data segments. It is crucial to monitor performance across all segments.

![](<../../../images/2023109\_course\_module1\_fin\_images.016-min.png>)

**Adversarial adaptation**. In the era of neural networks, models might face adversarial attacks. Monitoring helps detect these issues on time.

## Summing up

Many factors can impact the performance of an ML model in production. ML monitoring and observability are crucial to ensure that models perform as expected and provide value.
