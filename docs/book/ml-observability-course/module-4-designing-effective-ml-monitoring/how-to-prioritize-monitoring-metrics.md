# 4.2. How to prioritize ML monitoring metrics

{% embed url="https://youtu.be/jCXO4uuMHbs?si=9ss6_nK2bbLGq8Ph" %}

**Video 2**. [How to prioritize ML monitoring metrics](https://youtu.be/jCXO4uuMHbs?si=9ss6_nK2bbLGq8Ph), by Emeli Dral

## Which metrics to collect?

What exactly to log and which metrics to collect depend on your primary monitoring goal. 

For example, if you focus on **alerting**:
* Log a few metrics to be able to detect when things go wrong.
* Your main goal is to detect and alert on any issues quickly.

If you focus on **debugging and analysis**:
* Log additional context to understand and cover potential problems.
* Include not only main metrics but also some descriptive statistics to cover unknown unknowns. 

![](<../../../images/2023110\_course\_module4\_fin.018-min.png>)

## Metric hierarchy

Let us introduce a hierarchy of metrics you may collect. The hierarchy consists of five layers:
* **Symptoms** are key metrics that help identify model issues, e.g., 1-day accuracy or business KPIs. They are used to build alerts.
* **Summary metrics** provide additional context. It can be metrics like prediction volume, true positives, true negatives, share of missing data, etc. 
* **Input/output and performance profiling** give you more details, such as per-column descriptive statistics, distributions, segmented model performance, etc. 
* **Debugging and analytics data** include metrics for deeper analysis, like correlations and explainability. 
* **Raw data prediction logs** can be queried to calculate any custom metrics or build custom visualizations. 

![](<../../../images/2023110\_course\_module4\_fin.019-min.png>)

## Monitoring depth

Depending on your specific circumstances, you can choose minimalistic symptom-based monitoring: log less data and only look at a few metrics.   

**Minimalistic monitoring** is totally fine if you: 
* Have just **a few ML models** in production, 
* Work with **smaller datasets**,
* Deal with **less critical** use cases,
* Build your monitoring for **technical users** only,
* Can **easily access predictions** for any additional analysis,
* If the **prediction frequency** is low.

However, you might need more **in-depth monitoring** if you: 
* Have **multiple models in production** and want to standardize debugging and model support, 
* Work with **larger datasets**, and hence, it is expensive to query logs, 
* Deal with **critical use cases** where the cost of error is high, 
* Build your monitoring system for **business stakeholders**.

![](<../../../images/2023110\_course\_module4\_fin.020-min.png>)

**Is there a good default?** Monitoring is use-case specific. However, for each new model, you can start with a “middle ground” metric composition:
* Pick a few **key quality indicators** to use as issue symptoms to alert on.
* Add **per-column data summaries** and **performance summaries** to simplify immediate troubleshooting.

This can be a good go-to solution until you develop a monitoring approach that fits your specific use case. 

![](<../../../images/2023110\_course\_module4\_fin.021-min.png>)

## Metric prioritization 

Here is how you can prioritize metrics for your initial setup:
* Service health
* Model performance
* Data quality and integrity
* Data and concept drift

![](<../../../images/2023110\_course\_module4\_fin.023-min.png>)

**1. Service health**

Service health is a must-to-track as it forms a basis for all other metrics. It answers the question "Does the service work?" To track the service's health, you can use standard software performance metrics like latency, error rate, memory usage, disk usage, etc.

An important thing to add is monitoring the number of model predictions. This is especially relevant if you have fallback solutions such as alternative models or rule-based systems you use when the model does not respond or the incoming data has low quality. You need to know how often each model is used.

![](<../../../images/2023110\_course\_module4\_fin.025-min.png>)

**2. Model performance **

This set of metrics answers the question "How does the service perform?" and “Did anything break?” 

**Monitoring.** Depending on your use case, you can pick the best available signal to alert on: **direct** or **proxy metrics**. 

* **Direct**. You can measure business KPIs or direct model quality (accuracy, RMSE, etc.). 
* **Proxy**. If the ground truth is not available, you can switch to proxy metrics, e.g., use heuristics, check that output range compliance, or monitor output distribution drift. 

Make sure that your chosen KPIs are something you want to act upon if a certain threshold is reached. 

![](<../../../images/2023110\_course\_module4\_fin.028-min.png>)

**Debugging**. To simplify troubleshooting, you can also capture additional statistics like distribution output shape. For example, if the prediction drift is detected, you can see how the distribution of the model predictions has changed. You can also log data on model errors to analyze error buckets and error distribution. 

![](<../../../images/2023110\_course\_module4\_fin.029-min.png>)

**3. Data quality and data integrity**

If model performance issues are detected, data quality and integrity metrics help to understand where it has broken and whether you can trust your data. 

**Monitoring**. There are two methods you can use to analyze data quality and data integrity:
* **Track data health metrics**, such as the share of missing values, the share of duplicates, and the share of features out of range.
* **Run test suites** on top of data health metrics. You can periodically run scans with a large number of checks and track the number of failed tests. 

![](<../../../images/2023110\_course\_module4\_fin.033-min.png>)

**Debugging**. To log additional data for debugging purposes, you can capture dataset or column statistics – count, mean, standard deviation, min, max, etc. 

![](<../../../images/2023110\_course\_module4\_fin.034-min.png>)

**4. Data and concept drift**

This block of metrics helps to determine whether the model is still relevant.

**Monitoring**. To simplify the alerting and avoid false alerts, you can look at the following:
* Distribution drift in the most important features only.
* Prediction drift. 
* Overalldataset drift instead of drift in the individual features.

![](<../../../images/2023110\_course\_module4\_fin.036-min.png>)

**Debugging**. You can log feature distributions to compare them over time.

![](<../../../images/2023110\_course\_module4\_fin.037-min.png>)

## Comprehensive monitoring

Depending on the problem statement and model usage scenario, you can introduce more comprehensive monitoring metrics: 
* **Performance by segment**. It can be especially useful if you deal with a diverse audience or complex object structures and want to monitor them separately. 
* **Model bias and fairness**. These metrics are crucial for sensitive domain areas like healthcare.
* **Outliers**. Monitoring for outliers is vital when individual errors are costly.
* **Explainability**. Explainability is important when users need to understand model decisions/outputs.

![](<../../../images/2023110\_course\_module4\_fin.038-min.png>)

## Summing up

We discussed which metrics to collect when building a monitoring system and how to prioritize them. Here are some must-haves to keep in mind:
* Always monitor service health metrics. 
* Always store prediction logs, including inputs and outputs.
* Limit alerting to key metrics or symptoms.
* Define monitoring depth based on your specific needs. 
* When in doubt, go for the middle ground: select several metric groups – e.g., model quality, data quality, and data drift – and define the best signals for each group. 

Up next: dive into the retraining system and its connection to model performance and monitoring.
