---
description: What a good ML monitoring system is, and how to set up the logging architecture to capture metrics for further analysis.
---

# 4.1. Logging for ML monitoring

{% embed url="https://youtu.be/CtUsDcA3tB0?si=RNDR2uRZ7wc8NwxB" %}

**Video 1**. [Logging for ML monitoring](https://youtu.be/CtUsDcA3tB0?si=RNDR2uRZ7wc8NwxB), by Emeli Dral

## What is a good ML monitoring system?
A good ML monitoring system consists of three key components:
* **Instrumentation** to ensure collection and computation of useful metrics for analyzing model behavior and resolving issues.
* **Alerting** to define unexpected model behavior through metrics and thresholds and design action policy.
* **Debugging** to provide engineers with context to understand model issues for faster resolution.

![](<../../../images/2023110\_course\_module4\_fin.004-min.png>)

When it comes to ML monitoring setup, there is no “one size fits all.” Here are some factors that affect the ML monitoring architecture and choice of metrics:
* ML service implementation (online service vs. batch model).
* Environment stability.
* Feedback loop (immediate or delayed feedback).
* Team resources (capacity to implement and operate the ML monitoring system).
* Use case criticality.
* Scale and complexity of the ML system.

![](<../../../images/2023110\_course\_module4\_fin.005-min.png>)

## Logging and instrumentation

ML monitoring starts with logging. Before talking about metrics, you need to implement a way to collect the data for analysis. 

**Step 1. Capture service (event) logs**

Capturing service logs is a must-have for any production service, as it helps to monitor and debug service health. You may record different types of events that happen in your service. One will be the prediction event when the service gets the input data and returns the output. 

![](<../../../images/2023110\_course\_module4\_fin.008-min.png>)

**Step 2. Capture prediction logs**

When you record the prediction event, make sure to log all prediction-related information, including model input data, model output, and ground truth, if available. 

These prediction logs are the key input for ML model quality monitoring. You also need them for model retraining, debugging, and audits.

![](<../../../images/2023110\_course\_module4\_fin.009-min.png>)

**Step 3. Log ML monitoring metrics**

Logging architecture heavily depends on how you deploy your models.

![](<../../../images/2023110\_course\_module4\_fin.012-min.png>)

Typically, it involves a **prediction store** where prediction data is recorded. It requires long-term secure storage with features like backups.

Once you set up this prediction logging, here are two main approaches to **ML monitoring implementation**:
* **ML monitoring service** can pull data from the prediction store – or data can be pushed directly from the ML service – to compute monitoring metrics. 
* **Monitoring jobs** can be operated with the help of a pipeline manager and load data from the prediction store to compute monitoring metrics.

The next element is a **monitoring dashboard**:
* A **metric store** is created to store computed metrics. It needs quick querying capabilities for efficient dashboard interactions.
* The monitoring dashboard uses this metric store as the **data source** to visualize calculated metrics.

**For smaller datasets**, connecting the monitoring dashboard directly to the prediction store can suffice. It also works well if you run **ad-hoc or scheduled reports**.

## Summing up
We discussed setting up the logging architecture to capture useful metrics for further analysis. Next, we will cover what exactly to log.
