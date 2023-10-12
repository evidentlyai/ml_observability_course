# 2.6. Data and prediction drift in ML

{% embed url="https://www.youtube.com/watch?v=bMYcB_5gP4I&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=12" %}

**Video 6**. [Data and prediction drift in ML](https://www.youtube.com/watch?v=bMYcB_5gP4I&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=12), by Emeli Dral

## What is data drift, and why evaluate it?

When ground truth is unavailable or delayed, we cannot calculate ML model quality metrics directly. Instead, we can use proxy metrics like feature and prediction drift. 

**Prediction drift** shows changes in the distribution of **model outputs** over time. Without target values, this is the best proxy of the model behavior. Detected changes in the model outputs may be an early signal of changes in the model environment, data quality bugs, pipeline errors, etc. 

![](<../../../images/2023109\_course\_module2.058.png>)

**Feature drift** demonstrates changes in the distribution of **input features** over time. When we train the model, we assume that if the input data remains reasonably similar, we can expect similar model quality. Thus, data distribution drift can be an early warning about model quality decay, important changes in the model environment or user behavior, unannounced changes to the modeled process, etc. 

![](<../../../images/2023109\_course\_module2.060.png>)

Prediction and feature drift can serve as early warning signs for model quality issues. They can also help pinpoint a root cause when the model decay is already observed.

![](<../../../images/2023109\_course\_module2.065.png>)

Some key considerations about data drift to keep in mind:
* **Prediction drift is usually more important than feature drift**. If you monitor one thing, look at the outputs. 
* **Data drift in ML is a heuristic**. There is no “objective” drift; it varies based on the specific use case and data.
* **Not all distribution drift leads to model performance decay**. Consider the use case, the meaning of specific features, their importance, etc.
* **You don’t always need to monitor data drift**. It is useful for business-critical models with delayed feedback. But often you can wait.
* **Data drift helps with debugging**. Even if you do not alert on feature drift, it might help troubleshoot the decay.
* **Drift detection might be valuable even if you have the labels**. Feature drift might appear before you observe the model quality drop.

{% hint style="info" %}
**Further reading:** [How to break a model in 20 days. A tutorial on production model analytics](https://www.evidentlyai.com/blog/tutorial-1-model-analytics-in-production).  
{% endhint %}

## How to detect data drift?

To detect distribution drift, you need to pick:
* **Drift detection method**: statistical tests, distance metrics, rules, etc.
* **Drift detection threshold**: e.g., confidence levels for statistical tests or numeric threshold for distance metrics. 
* **Reference dataset**: what an exemplary distribution is.
* **Alert conditions**: e.g., based on feature importance and the share of the drifting features.

## Data drift detection methods

There are three commonly used approaches to drift detection:
* **Statistical tests**, e.g., Kolmogorov-Smirnov or Chi-squared test. You can use parametric or non-parametric tests to compare distributions. Generally, parametric tests are more sensitive. Using statistical tests for drift detection is best for smaller datasets and samples. The resulting drift “score” is measured by p-value (a “confidence” of drift detection). 
* **Distance-based metrics**, e.g., Wasserstein distance or Jensen Shannon Divergence. This group of metrics works well for larger datasets. The drift “score” is measured as distance, divergence, or level of similarity. 
* **Rule-based checks** are custom rules for detecting drift based on heuristics and domain knowledge. These are great when you expect specific changes, e.g., new categories added to the dataset. 

Here is how the defaults are implemented in the Evidently open-source library.

**For small datasets (<=1000)**, you can use Kolmogorov-Smirnov test for numerical features, Chi-squared test for categorical features, and proportion difference test for independent samples based on Z-score for binary categorical features. 

![](<../../../images/2023109\_course\_module2.070.png>)

**For large datasets (>1000)**, you might use Wasserstein Distance for numerical features and Jensen-Shannon divergence for categorical features.

![](<../../../images/2023109\_course\_module2.071.png>)
