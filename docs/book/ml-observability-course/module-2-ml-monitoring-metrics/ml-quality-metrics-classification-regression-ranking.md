# 2.2. Overview of ML quality metrics. Classification, regression, ranking

{% embed url="https://www.youtube.com/watch?v=4_LOXDWxCbw&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=8" %}

**Video 2**. [Overview of ML quality metrics](https://www.youtube.com/watch?v=4_LOXDWxCbw&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=8), by Emeli Dral

## ML model quality in production

ML model quality degrades over time. This happens because things change, and the model’s environment evolves. 

You need **monitoring** to be able to maintain the ML model's relevance by detecting issues on time. You can also collect additional data and build visualizations for **debugging**. 

But there is a caveat: to calculate classification, regression, and ranking quality metrics, **you need labels**. If you can, consider labeling at least part of the data to be able to compute them. 

![](<../../../images/2023109\_course\_module2.009.png>)

## Classification quality metrics

A classification problem in ML is a task of assigning predefined categories or classes (labels) to new input data. Here are some commonly used metrics to measure the quality of the classification model:
* [**Accuracy**](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall) is the overall share of correct predictions. It is well-interpretable and arguably the most popular metric for classification problems. However, be cautious when using this metric with imbalanced datasets.
* [**Precision**](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall) measures correctness when predicting the target class.
* [**Recall**](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall) shows the ability to find all the objects of the target class. Precision and recall are usually used together. Both work well for unbalanced datasets.
* **F1-score** is the harmonic mean of precision and recall.
* [**ROC-AUC**](https://www.evidentlyai.com/classification-metrics/explain-roc-curve) works for probabilistic classification and evaluates the model's ability to rank correctly.
* **Logarithmic loss** demonstrates how close the prediction probability is to the actual value. It is a good metric for probabilistic problem statement. 

![](<../../../images/2023109\_course\_module2.012.png>)

Methods to help visualize and understand classification quality metrics include:
* [**Confusion matrix**](https://www.evidentlyai.com/classification-metrics/confusion-matrix) shows the number of correct predictions – true positives (TP) and true negatives (TN) – and the number of errors – false positives (FP) and false negatives (FN). You can calculate precision, recall, and F1-score based on these values.
* **Precision-recall table** helps calculate metrics like precision, recall, and F1-score for different thresholds in probabilistic classification.
* **Class separation quality** helps visualize correct and incorrect predictions for each class.
* **Error analysis**. You can also map predicted probabilities or model errors alongside feature values and explore if a specific type of misclassification is connected to the particular feature values.

[](<../../../images/2023109\_course\_module2.016.png>)

{% hint style="info" %}
**Further reading:** [What is your model hiding? A tutorial on evaluating ML models](https://www.evidentlyai.com/blog/tutorial-2-model-evaluation-hr-attrition).  
{% endhint %}

## Regression quality metrics

Regression models provide numerical output which is compared against actual values to estimate ML model quality. Some standard regression quality metrics include:
* **Mean Error (ME)** is an average of all errors. It is easy to calculate, but remember that positive and negative errors can overcompensate each other.
* **Mean Absolute Error (MAE)** is an average of all absolute errors.
* **Root Mean Squared Error (RMSE)** is a square root of the mean of squared errors. It penalizes larger errors.
* **Mean Absolute Percentage Error (MAPE)** averages all absolute errors in %. Works well for datasets with objects of different scale (i.e., tens, thousands, or millions).
* **Symmetric MAPE** provides different penalty for over- or underestimation.

[](<../../../images/2023109\_course\_module2.020.png>)

Some of the methods to analyze and visualize regression model quality are:
* **Predicted vs. Actual** value plots and Error over time plots help derive patterns in model predictions and behavior (e.g., Does the model tend to have bigger errors during weekends or hours of peak demand?). 
* **Error analysis**. It is often important to distinguish between **underestimation** and **overestimation** during error analysis. Since errors might have different business costs, this can help optimize model performance for business metrics based on the use case. 

You can also map extreme errors alongside feature values and explore if a specific type of error is connected to the particular feature values. 

[](<../../../images/2023109\_course\_module2.025.png>)

## Ranking quality metrics

Ranking focuses on the relative order of items rather than their absolute values. Popular examples of ranking problems are search engines and recommender systems. 

We need to estimate the order of objects to measure quality in ranking tasks. Some commonly used ranking quality metrics are:
* **Cumulative gain** helps estimate the cumulative value of recommendations and does not take into account the position of a result in the list.
* **Discounted Cumulative Gain (DCG)** gives a penalty when a relevant result is further in the list. 
* **Normalized DCG (NDCG)** normalizes the evaluation irrespective of the list length.
* **Precision @k** is a share of the relevant objects in top-K results.
* **Recall @k** is a coverage of all relevant objects in top-K results.
* **Lift @k** reflects an improvement over random ranking.

[](<../../../images/2023109\_course\_module2.028.png>)

If you work on a recommender system, you might want to consider additional – “beyond accuracy” – metrics that reflect RecSys behavior. Some examples are:
* Serendipity
* Novelty 
* Diversity 
* Coverage
* Popularity bias

You can also use other custom metrics based on your problem statement and business context, for example, by weighting the metrics by specific segments.

## Considerations for production ML monitoring

When you define the model quality metrics to monitor the ML model performance in production, there are some important considerations to keep in mind:

**Pick the right metrics that align with your use case and business goals**:
* **The usuals apply**. E.g., reuse metrics from the model development phase and do not use accuracy for a problem with highly imbalanced classes.
* **Consider a proxy business metric to evaluate impact**. E.g., consider tracking an estimated loss/gain based on known error costs, the share of predictions with an error larger than X, etc.
* **Not all evaluation metrics are useful for dynamic production monitoring**. E.g., ROC AUC reflects quality across all thresholds, but a production model has a specific one.
* **Consider custom metrics or heuristics**. E.g., the average position of the first relevant object in the recommendation block.

**It’s not just a choice of metric**. There are other parameters you might need to define:
* **Aggregation window**. It is crucial to calculate metrics in the right windows. Depending on the use case, you might want to monitor precision, for example, every minute, hourly, daily, or over a sliding 7-day window as a key performance indicator.
* **Segments**. You can track model quality separately for different locations, devices, customer subscription types, etc.

## Summing up

We discussed the importance of monitoring ML model performance in production and introduced commonly used quality metrics for classification, regression, and ranking problems. 

Further reading: [What is your model hiding? A tutorial on evaluating ML models](https://www.evidentlyai.com/blog/tutorial-2-model-evaluation-hr-attrition).

In the next part of this module, we will dive into practice and build a model quality report using the open-source [Evidently](https://github.com/evidentlyai/evidently) Python library.
