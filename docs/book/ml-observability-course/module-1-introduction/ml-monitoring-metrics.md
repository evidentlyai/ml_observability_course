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

![](<../../../images/2023109\_course\_module1\_fin\_images.034.png>)

For a deeper dive into **ML model quality and relevance** and **data quality and integrity** metrics, head to [Module 2](../module-2-ml-monitoring-metrics.md).
