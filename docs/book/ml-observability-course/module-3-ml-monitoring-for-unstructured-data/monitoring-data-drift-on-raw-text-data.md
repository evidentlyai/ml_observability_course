---
description: How to detect and evaluate raw text data drift using domain classifier and topic modeling.
---

# 3.2. Monitoring data drift on raw text data

{% embed url="https://www.youtube.com/watch?v=wHyXSyVg5Ag&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=16" %}

**Video 2**. [Monitoring data drift on raw text data](https://www.youtube.com/watch?v=wHyXSyVg5Ag&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=16), by Emeli Dral

## Challenges of monitoring raw text data

Handling raw text data is more complex than dealing with structured tabular data. With structured data, you can usually define “good” or “expected” data, e.g., particular feature distributions or statistical values can signal the data quality. For unstructured data, there is no straightforward way to define data quality or extract a signal for raw text data. 

When it comes to data drift detection, you can use two strategies that rely on raw text data: **domain classifier** and **topic modeling**.

![](<../../../images/2023109\_course\_module3.011-min.png>)

## Domain classifier

**Domain classifier** method or **model-based drift detection** uses a classifier model to compare distributions of reference and current datasets by training a model that predicts to which dataset a specific text belongs. If the model can confidently identify which text samples belong to the current or reference dataset, the two datasets are probably sufficiently different.

{% hint style="info" %}
**Further reading:** this approach is described in more detail in the paper ["Failing loudly: An Empirical Study of Methods for Detecting Dataset Shift"](https://arxiv.org/abs/1810.11953).
{% endhint %}

![](<../../../images/2023109\_course\_module3.013-min.png>)

You can directly use the ROC AUC of the binary classifier as the “drift score” when you deal with **large datasets**. If you work with **smaller datasets** (< 1000), you can compare the model ROC AUC against a random classifier. 

The benefit of using model-based drift detection on raw data is its **interpretability**. In this case, you can identify top words and text examples that were easy to classify to explain the drift and debug the model. 

![](<../../../images/2023109\_course\_module3.014-min.png>)

{% hint style="info" %}
**Further reading:** [Monitoring NLP models in production: a tutorial on detecting drift in text data](https://www.evidentlyai.com/blog/tutorial-detecting-drift-in-text-data).
{% endhint %}

## Topic modeling

Another strategy for evaluating raw data quality is **topic modeling**. The goal here is to categorize text into interpretable topic clusters, so instead of a binary classification model, we use a **clustering model**. 

How it works:
* Apply the clustering model to new batches of data.
* Monitor the size and share of different topics over time.
* Changes in topics can indicate data drift.

Using this method can be challenging due to difficulties in building a good clustering model:
* There is no ideal structure in clustering.
* Typically, it requires manual tuning to build accurate and interpretable clusters.

![](<../../../images/2023109\_course\_module3.018-min.png>)

## Summing up

Defining data quality and tracking data drift for text data can be challenging. However, we can extract interpretable signals from text data to detect drift. You can use such methods as domain classifier and topic modeling to monitor for drift and evaluate the quality of raw text data. 

Further reading:
* [Failing loudly: An Empirical Study of Methods for Detecting Dataset Shift](https://arxiv.org/abs/1810.11953)
* [Monitoring NLP models in production: a tutorial on detecting drift in text data](https://www.evidentlyai.com/blog/tutorial-detecting-drift-in-text-data)

Up next: an exploration of alternative text drift detection methods that use descriptors.
