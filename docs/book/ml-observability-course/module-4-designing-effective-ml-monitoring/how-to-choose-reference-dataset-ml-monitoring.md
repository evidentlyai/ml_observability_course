---
description: What a reference dataset is in ML monitoring, how to choose one for drift detection, and when to use multiple references.
---

# 4.4. How to choose a reference dataset in ML monitoring

{% embed url="https://youtu.be/42J-C4WmkZc?si=Av1gwZXAkBZXDT70" %}

**Video 4**. [How to choose a reference dataset in ML monitoring](https://youtu.be/42J-C4WmkZc?si=Av1gwZXAkBZXDT70), by Emeli Dral

## Why use a reference dataset?

There are two main uses for a reference dataset. 

1. You can use it **to derive test conditions automatically**, saving time and effort in setting up tests manually. 

For example, you can use a reference dataset to generate conditions for data quality checks (to track feature ranges, share of missing values, etc.) and model quality checks (to keep tabs on metrics like precision and accuracy) by passing a previous batch of data as a reference. 

2. You can use a reference dataset **as a baseline to detect data and prediction drift** in production by comparing new data distributions against reference distributions.

Reference dataset also can be used to **detect training-serving skew** as it provides a baseline to detect changes between training and production data. 

![](<../../../images/2023110\_course\_module4\_fin.064-min.png>)

## What makes a good reference dataset?

Characteristics of a **good reference dataset**:
* Reflects realistic data patterns, including cycles and seasonality.
* Contains a large enough sample to derive meaningful statistics.
* Includes realistic scenarios (e.g., sensor outages) to validate against new data.

What a **reference dataset is not**:
* It is **not the same as a training dataset**. You can sometimes choose training data to be your reference, but they are not synonymous.  
* It is **not a “golden dataset,”** which serves a different purpose.

![](<../../../images/2023110\_course\_module4\_fin.065-min.png>)

You always need a reference dataset if your goal is to compare distributions to detect data or prediction drift (e.g., using metrics like Wasserstein distance). 

However, having a reference dataset is not a must:
* You can run one-sample statistical tests that don't require a comparison of distributions.
* For most types of checks, you can manually specify test conditions, such as min-max feature ranges. This works well if you have a limited set of data with known expected behaviors.

However, using a reference dataset is a great hack to automate generating test conditions! 

## Using training data as a reference

Using training data as a reference can be acceptable in specific contexts but is generally not recommended due to pre-processing and potential biases.

**If the training data is all you have**, it is OK to use it for the following types of checks:
* To derive feature types and data schema.
* To derive feature ranges (num) and value lists (cat).
* To derive feature correlations.
* To detect training-serving skew.
						
**It is less optimal for**:
* Generating expectations about model quality.
* Deriving data on e.g., share of nulls.
* Using it as a baseline for drift detection. 

You can consider using hold-out validation data or previous batches of data instead.

![](<../../../images/2023110\_course\_module4\_fin.068-min.png>)

## Reference dataset for drift detection

When choosing a reference dataset for drift detection, make sure to pick a representative dataset that captures typical distributions and variations in the data. You can use historical data to decide on the appropriate windows; for example, you can compare the data using monthly, weekly, or daily windows. 

![](<../../../images/2023110\_course\_module4\_fin.069-min.png>)

You should make the following decisions:
* **What do you compare against?** You can use training data (generally not recommended), validation, and previous production batches.
* **What batch size to use?** You need to determine the size of current and reference datasets for effective comparison – 1 day, 1 week, 1 year, 1000 objects, etc. 
* **How to update reference data?** You can have a static reference (e.g., which you update once a month) or shift the reference data dynamically (e.g., sliding window approach).

![](<../../../images/2023110\_course\_module4\_fin.071-min.png>)

Analyzing historical data can help determine the most effective reference data strategy. 

{% hint style="info" %}
**Further reading:** [How to detect, evaluate and visualize historical drifts in the data](https://www.evidentlyai.com/blog/tutorial-3-historical-data-drift).
{% endhint %}

**Multiple references**. It often makes sense to use multiple reference datasets. For example, you can have multiple comparison windows to capture seasonality and cyclic trends:

![](<../../../images/2023110\_course\_module4\_fin.073-min.png>)

**Sampling vs. entire dataset**. If you have large datasets, you can consider using sampling, for example, random or stratified sampling.
* **Sampling is great for drift detection**. In fact, all statistical tests were made to work with samples! It can save you computational resources and allow for faster results calculation. If you look to detect a statistical distribution shift in the overall dataset, sampling is totally fine. 
* **For detecting data quality anomalies, full datasets are preferable**. If you look for data quality issues – e.g., individual outliers or duplicates – sampling can disguise them. 

![](<../../../images/2023110\_course\_module4\_fin.074-min.png>)

## Summing up

* There is no “universal” reference dataset. It should be tailored to the specific use case and expectations of similarity to current data.
* Hold-out validation data is preferred over training data for creating reference datasets, especially for drift detection. Use training data only if there is nothing else. 
* It is crucial to account for seasonality and historical patterns when choosing the reference dataset to ensure that it accurately represents the expected variations in data.
* Historical data is a valuable resource for informing reference dataset selection.

Further reading: [How to detect, evaluate and visualize historical drifts in the data](https://www.evidentlyai.com/blog/tutorial-3-historical-data-drift)

Up next: custom metrics for ML monitoring. 
