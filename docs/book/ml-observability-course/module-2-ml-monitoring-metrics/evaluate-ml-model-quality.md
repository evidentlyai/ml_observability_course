---
description: How to evaluate ML model quality directly and use early monitoring to detect potential ML model issues.
---

# 2.1. How to evaluate ML model quality

{% embed url="https://www.youtube.com/watch?v=7Y819MAQTDg&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=7" %}

**Video 1**. [How to evaluate ML model quality](https://www.youtube.com/watch?v=7Y819MAQTDg&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=7), by Emeli Dral

## Challenges of standard ML monitoring

When it comes to standard ML monitoring, we usually start by measuring ML model performance metrics: 
* **Model quality and error metrics** show how the ML model performs in production. For example, you can track precision, recall, and log-loss for classification models or MAE for regression models.
* **Business or product metrics** help evaluate the ML model’s impact on business performance. You might want to track such metrics as purchases, clicks, views, etc. 

**However, standard ML monitoring is not always enough**. Some challenges can complicate the ML performance assessment:
* **Feedback or ground truth is delayed**. When ground truth is not immediately available, calculating quality metrics can be technically impossible.
* **Past performance does not guarantee future results**, especially when the environment is unstable.
* **Many segments with different quality**. Aggregated metrics might not provide insights for diverse user/object groups. In this case, we need to monitor quality metrics for each segment separately.
* **The target function is volatile**. Volatile target function can lead to fluctuating performance metrics, making it difficult to differentiate between local quality drops and major performance issues. 

![](<../../../images/2023109\_course\_module2.005-min.png>)

## Early monitoring metrics

You can adopt **early monitoring** together with standard monitoring metrics to tackle these challenges. 

Early monitoring focuses on metrics derived from consistently available data: input data and ML model output data. For example, you can track:
* **Data quality** to detect issues with data quality and integrity.
* **Data drift** to monitor changes in the input feature distributions.
* **Output drift** to observe shifts in model predictions.

![](<../../../images/2023109\_course\_module2.006-min.png>)

## Module 2 structure

This module includes both theoretical parts and code practice for each of the evaluation types. Here is the module structure:

**Model quality**
* Theory: ML model quality metrics for regression, classification, and ranking problems.
* Practice: building a sample report in Python showcasing quality metrics.
  
**Data quality**
* Theory: data quality metrics.
* Practice: creating a sample report in Python on data quality.

**Data and prediction drift**
* Theory: an overview of the data drift metrics.
* [OPTIONAL] Theory: a deeper dive into data drift detection methods and strategies.
* Practice: building a sample report in Python to detect data and prediction drift for various data type.

![](<../../../images/2023109\_course\_module2.007-min.png>)

## Summing up

Tracking ML quality metrics in production is crucial to ensure that ML models perform reliably in real-world scenarios. However, standard ML performance metrics like model quality and error are not always enough. 

Adopting early monitoring and measuring data quality, data drift, and prediction drift provides insights into potential issues when standard performance metrics cannot be calculated.

Through this module, learners will gain a theoretical understanding and hands-on experience in evaluating and interpreting model quality, data quality, and data drift metrics.
