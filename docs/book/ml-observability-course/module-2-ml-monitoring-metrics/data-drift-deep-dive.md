# 2.7. Deep dive into data drift detection [OPTIONAL]

{% embed url="https://www.youtube.com/watch?v=N47SHSP6RuY&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=13" %}

**Video 7**. [Data and prediction drift in ML](https://www.youtube.com/watch?v=N47SHSP6RuY&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=13), by Emeli Dral

Welcome to the deep dive into data drift detection! We will cover the following topics:

**Data drift detection methods:**
* More on methods to detect data drift
* Strategies for choosing drift detection approach

**Special cases:**
* Detecting drift for large datasets
* Detecting drift for real-time models
* Using drift as a retraining trigger

**Useful tips:**
* How to interpret prediction and data drift together?
* What to do after drift is detected

## Drift detection methods

Let’s have a closer look at the commonly used approaches to drift detection.

**Parametric statistical tests**
There are both **one-sample** and **two-sample** parametric tests.: 
* **If you only have current data** and no reference data is available, you can use **Z-test and T-test for mean** (m = m0) or **one-proportion Z-test** (p = p0) to detect data drift. These methods can work if you have interpretable features – e.g., salary or age – as you need to develop the hypotheses on distribution values.  
* **If reference data is available**, you can use two-sample parametric tests to compare distributions: for example, **two-proportions Z-test** or **two-sample Z-test and T-test for means** (for normally distributed samples). 

Some considerations to keep in mind when using parametric tests:
* **They require different tests for different features.** For example, some tests assume that your data are normally distributed.  
* **They are more sensitive to drift than non-parametric tests.** If you work on a problem where you have a small dataset and want to react to even minor deviations  – it makes sense to use parametric tests. 
* **Hard to fine-tune if you have a lot of features.** If you have many features with different feature types, you need to invest a lot of time in choosing the right test for each feature. 

It makes sense to use parametric tests if you have a small number of interpretable features and work on critical use cases (e.g., in healthcare).

![](<../../../images/2023109\_course\_module2.081-min.png>)

**Non-parametric statistical tests**
Non-parametric tests are less demanding to the properties of data samples and thus are widely used. Examples include **Kolmogorov-Smirnov** test, K-sample **Anderson-Darling** test, **Pearson’s chi-squared** test, **Fisher’s/Barnard’s** exact test for small samples, etc. 

When using non-parametric tests, consider the following:
* **Feature type.** You can use heuristics to choose suitable tests based on the feature type, e.g., numerical, categorical, or binary.
* **Sensitivity.** Non-parametric tests are less sensitive to drift than parametric tests.
* **Data volumes.** It makes sense to use non-parametric tests for low-volume datasets or samples (e.g., less than 1000 objects).

![](<../../../images/2023109\_course\_module2.082-min.png>)

**Distance-based approaches**
Distance-based methods measure how far two distributions are from each other and thus are easy to interpret. For example, you can calculate **Wasserstein distance**, **Jensen-Shannon divergence**, or **Population Stability Index** (PSI).

Some considerations to keep in mind when using distance-based methods to detect data drift:
* **Variety of metrics is available.** Roughly any metric that shows difference/similarity between distributions can be used as a drift detection method.
* **High interpretability compared to statistical tests.** Often, it makes more sense to pick an interpretable metric rather than a statistical test.
* **Data volume.** It makes sense to use distance-based methods for larger datasets (e.g., > 1000 objects).

![](<../../../images/2023109\_course\_module2.083-min.png>)

**Domain classification**
This approach uses binary classifiers to distinguish between reference and current data. It can be used to detect data drift in different data types, including embeddings, unstructured data (such as texts), and multimodal data. 

{% hint style="info" %}
**Further reading:** [Which test is the best? We compared 5 methods to detect data drift on large datasets](https://www.evidentlyai.com/blog/data-drift-detection-large-datasets).  
{% endhint %}

## How to choose a drift detection approach?

**Data drift detection is a heuristic.** There is no strict law. This is why it is important that you consider why you want to detect drift, and what method might make sense for you. 

Consider your problem statement and dataset properties. For example:
* If your use case is sensitive, you might want to use parametric tests.
* If interpretability is important, consider distance-based methods.
* Domain classification can be a good choice if you work with various data types – text, videos, tabular data. 

To choose the right drift detection approach for your particular problem statement, you can consider two options:

**1. Go with defaults.**

In this scenario, you pick some reasonable defaults to start and adjust the sensitivity as you proceed with monitoring. 
* Start with basic assumptions. Do you want to detect drift for the whole dataset or only consider drift in important features?
* Pick reasonable metrics and thresholds. For example, for numerical features, you can pick Wasserstein Distance at 0.1 threshold. 
* Start monitoring. 
* Visualize results. 
* Adjust based on false alarms, sensitivity, and drift interpretations. 

**2. Experiment.**

In this scenario, you use historical data to tweak detection parameters using past known drifts. Here is an example of an experiment:
* Take data for a stable period
* Take data with known drift or simulate drift using synthetic data.
* Apply different drift detection approaches. Experiment with tests, thresholds, window size and/or bucketing parameters. 
* Choose the optimal approach that detects known drifts and minimizes false alarms.

## Special cases
There are some special cases to keep in mind when detecting data drift:

**Large datasets.**
Statistics was made to work with samples. Having many objects and/or features in a dataset can lead to some tests being “too sensitive” or taking too long to compute. If this is the case, you can use **sampling** to pick representative observations and apply tests on top of them. Alternatively, you can try **bucketing** to aggregate observations and reduce the amount of data. For example, you can detect drift on top of hourly data instead of minutely. 

![](<../../../images/2023109\_course\_module2.089-min.png>)

**Non-batch models.**
While some metrics can be calculated in real-time, we need to generate a batch of data to detect data drift. 

The solution is to use **window functions** to perform tests on continuous data streams. You can pick a window function (i.e., moving windows with/without moving reference), choose the window and step size to create batches for comparison, and “compare” the windows. 

![](<../../../images/2023109\_course\_module2.090-min.png>)

**Feature drift as a retraining trigger.**
There are both pros and cons of using drift detection as the retraining trigger.

Generally, we do not recommend retraining a model every time the drift is detected because:
* **Data might be low-quality.** Retraining the model on corrupted data will be useless if data drift occurs due to data processing issues.
* **Data might be insufficient.** Sometimes, we just don’t have enough data for new model training. 
* **Data might be non-representative.** Look out for unstable periods, e.g., pandemic, seasonal spikes, etc.

Instead, try to understand data drift first:
* **Data drift as an investigation trigger.** Try to figure out the root cause of the detected drift. 
* **Data drift as a labeling trigger.** You can use a data drift signal to start the labeling process to be able to compute the actual model quality metrics.

If you use data drift as a retraining trigger, it is critical to implement a solid evaluation process before roll-out to make sure the new model performs well.

![](<../../../images/2023109\_course\_module2.091-min.png>)

## How to interpret data and prediction drift together?

It often makes sense to monitor both prediction drift (change in the model outputs) and data drift (change in the model features). 

However, data and prediction drift do not necessarily mean that something is wrong. Let’s look at two examples of data and prediction drift detected together or independently. 

**Scenario 1. Data drift: detected. Prediction drift: not detected.** 
There are both positive and negative ways to interpret it.

**Positive interpretation:**
* Important features did not change. 
* Model is robust enough to survive drift. 
* No need to intervene.

**Negative interpretation:**
* Important features changed. 
* Model should have reacted but did not. It does not extrapolate well.
* We need to intervene.

**Scenario 2. Data drift: detected. Prediction drift: detected.** 
Again, there are positive and negative ways of interpreting it.

**Positive interpretation:**
* Important features changed. 
* Model reacts and extrapolates well (e.g., prices lower -> higher sales) 
* No need to intervene.

**Negative interpretation:**
* Important features changed. 
* Model behavior is unreasonable.
* We need to intervene.

## What to do if drift is detected?

Here are some possible steps to take if the drift is detected:

**1. Check the data quality.**
Make sure the drift is “real” and try to interpret where the drift is coming from. Data entry errors, stale features, and lost data are data quality issues disguised as data drift. If this is the case, fix the data first.

![](<../../../images/2023109\_course\_module2.098-min.png>)

**2.  Investigate the drift.**
Analyze which features have changed and how much. To understand the shift, you can:
* Visualize distributions
* Analyze correlation changes
* Check descriptive stats
* Evaluate segments
* Seek real-world explanations (e.g., a new marketing campaign)
* Team up with domain experts

![](<../../../images/2023109\_course\_module2.100-min.png>)

**3.  Doing nothing is also an option.** 
You might treat the drift as a false alarm, be satisfied with how the model handles drift, or simply decide to wait.

![](<../../../images/2023109\_course\_module2.101-min.png>)

**4.  Actively reacting to drift.** 
However, often, we need to react when the drift is detected:
* **Retrain the model.** Get new labels and actual values and re-fit the same model on the latest data. 
* **Rebuild the model.** If the change is significant, you might need to rebuild the training pipeline and test new model architectures.
* **Tune the model.** For example, you can change a threshold for drift detection. 
* **Use a fallback strategy.** Decide without ML: switch to manual processing, heuristics, or non-ML models.

![](<../../../images/2023109\_course\_module2.102-min.png>)

{% hint style="info" %}
**Further reading:** ["My data drifted. What's next?" How to handle ML model drift in production.](https://www.evidentlyai.com/blog/ml-monitoring-data-drift-how-to-handle).  
{% endhint %}

## Summing up

We discussed different drift detection methods and how to choose the optimal approach for your dataset and problem statement. We covered special cases like handling large datasets, calculating drift for real-time models, and using drift as a retraining trigger. We also learned how to interpret data and prediction drift and what to do if drift is detected.

Further reading: 
* [Which test is the best? We compared 5 methods to detect data drift on large datasets](https://www.evidentlyai.com/blog/data-drift-detection-large-datasets)
* ["My data drifted. What's next?" How to handle ML model drift in production.](https://www.evidentlyai.com/blog/ml-monitoring-data-drift-how-to-handle)

Up next: code practice on how to detect data drift using the open-source [Evidently](https://github.com/evidentlyai/evidently) Python library.
