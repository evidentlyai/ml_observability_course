---
description: A brief introduction to different types of tests and testing conditions and how to incorporate them in data and ML pipelines.
---

# 5.1. Introduction to data and ML pipeline testing

{% embed url="https://youtu.be/v7YW97YJ5DA?si=mEzSmfoTjDFxHF28" %}

**Video 1**. [Introduction to data and ML pipeline testing](https://youtu.be/v7YW97YJ5DA?si=mEzSmfoTjDFxHF28), by Emeli Dral

## When to perform testing

ML lifecycle involves various steps that require testing to ensure that our ML models function properly. Critical areas to test include the following steps of the ML lifecycle:
* During the feature engineering stage: testing the input data quality as it affects the whole pipeline.
* During model training (or retraining): model quality checks. 
* During model serving: validating incoming data and model outputs.
* During performance monitoring: continuously testing the model quality to detect and resolve potential issues.

![](<../../../images/202310\_module5\_fin.007-min.png>)

## How to perform testing

There are different types of checks you can use to test data and ML pipelines:

**Individual tests**
A test is a **metric** with a condition. You can perform a certain evaluation or measurement on top of a data batch and compare it against a threshold or expectation. You can formulate almost anything as a test: assertions on feature values, expectations about model quality on a specific segment, etc. Whatever you can measure, you can design as a test. 

Tests can be **column-level** (when metrics are calculated for a specific feature or column) or **dataset-level** (in this case, you calculate metrics for the whole dataset).

![](<../../../images/202310\_module5\_fin.010-min.png>)

**Test suites**
Individual tests can be grouped into test suites. For each test in a test suite, you can define test criticality and set alerting conditions: for example, based on the number of failed critical tests.

![](<../../../images/202310\_module5\_fin.011-min.png>)

When you create a test, you must define the test conditions. There are two main strategies you can use for establishing test conditions: 

**Reference-based conditions**
You can use a reference dataset to derive conditions automatically rather than set conditions manually for each individual test. This is a great option for certain types of checks, such as testing column types (which are easy to derive from a reference example) and for ad hoc testing such as when you import a new batch of data and can immediately visually explore the test results. However, be careful when designing alerting, as auto-generated test conditions are not perfect and may be prone to false alerts or missed issues.

![](<../../../images/202310\_module5\_fin.013-min.png>)

**Manually defined conditions**
With this approach, you specify conditions for each test manually. This method does not require additional data and can be great for encoding specific conditions based on domain expertise. 

![](<../../../images/202310\_module5\_fin.015-min.png>)

You can also combine reference-based and manual conditions. For example, you can manually pass conditions for specific features and use a reference dataset to define test conditions for the rest of your dataset. Combining these approaches is possible with tools like [Evidently](https://github.com/evidentlyai/evidently).

## Test automation

If you want to test your data and ML models continuously, switching from ad-hoc checks to automated testing is a good idea. You can use workflow managers like Airflow, Kubeflow, or Prefect to automate testing as part of the ML pipeline. If you run your ML model in batch, just add a testing step to your pipeline.

![](<../../../images/202310\_module5\_fin.016-min.png>)

## Recording test results

If you already use logging tools like MLflow, you can use them to log test results as well. Evidently also offers a monitoring dashboard where you can visualize individual and aggregate test results to track them in time. 

![](<../../../images/202310\_module5\_fin.017-min.png>)

## Example use case

The practical part of the module involves applying data and model quality tests on a toy dataset. Using the Bank marketing dataset, we will predict subscription outcomes from a marketing campaign. Data source: [bank marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing).

![](<../../../images/202310\_module5\_fin.019-min.png>)

You will design training and prediction pipelines as part of the code practice. For the **training pipeline**, you will prepare data, calculate features, do model training and scoring, and incorporate data, feature and model quality checks.

For the **prediction pipeline**, you will simulate the production usage of the model in a batch scenario. You will also implement data quality and stability checks, score model output, validate model quality, and use quality checks to make informed decisions on model retraining.

![](<../../../images/202310\_module5\_fin.021-min.png>)

And now, to practice!
