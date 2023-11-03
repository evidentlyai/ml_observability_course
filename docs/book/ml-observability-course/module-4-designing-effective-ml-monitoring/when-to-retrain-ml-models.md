# 4.3. When to retrain machine learning models

{% embed url="https://youtu.be/oqyyVp-t5A8?si=u-DeeyxCx9fBjs1_" %}

**Video 3**. [When to retrain machine learning models](https://youtu.be/oqyyVp-t5A8?si=u-DeeyxCx9fBjs1_), by Emeli Dral

## Why retrain ML models?

ML model quality degrades with time. It happens due to changes in the environment models operate within. The goal of ML monitoring is to help detect when the ML model’s quality starts to degrade, intervene, and get the ML service back on track. 

The good news is that new data is accumulated during model use. You can use this data to retrain and update your model.

![](<../../../images/2023110\_course\_module4\_fin.042-min.png>)

## Model retraining strategies

We will cover the two most widely used retraining strategies: scheduled retraining and trigger-based retraining. 

**Scheduled retraining**
This approach is straightforward: define a retraining schedule – daily, weekly, or monthly – and stick to it. The optimal schedule depends on the use case and data stability. This approach is a good enough solution to start with. 

**Pros**: 
* Simplicity in execution; no need to overthink.
**Cons**: 
* Resource-intensive. 
* May require complex infrastructure for model evaluation and deployment automation.
* More expensive support for automated retraining and deployment.
* Sometimes, it can make things worse if you don’t have a solid procedure for model evaluation in place. You risk deploying a model that is worse than the current one. 

![](<../../../images/2023110\_course\_module4\_fin.045-min.png>)

**Pro-tip for scheduled retraining**: use historical data to determine the rate of model decay and the volume of new data required for effective retraining. For example, you can get a training set from your historical data and train a model on top of this dataset. Then, you can start experimenting: apply this model to new batches of data with a certain time step – daily, weekly, monthly – to measure how the model performs on the new data and define when its quality starts to degrade. You can also run checks on historical data to define:
* Will more data improve model quality?
* How quickly does the quality degrade?
* How much data is needed to retrain the model?
* Should you drop the old data when retraining?

**Important note**: you need labels to do it. If feedback/ground truth is not available yet, it makes sense to send data for labeling before you start experimenting with historical data. 

![](<../../../images/2023110\_course\_module4\_fin.046-min.png>)

{% hint style="info" %}
**Further reading:** [To retrain, or not to retrain? Let's get analytical about ML model updates](https://www.evidentlyai.com/blog/retrain-or-not-retrain).
{% endhint %}

**Trigger-based retraining**
To use this strategy, you need to pick a key metric – e.g., daily accuracy – and retrain the model if this metric breaks a certain threshold. For example, the retraining trigger may be “retrain the model if daily accuracy drops under 0.9.”

**Pros**: 
* Allows retraining the model automatically. 
* Works well for costly updates and complex approvals, as retraining is based on specific performance metric drops.
**Cons**: 
* Requires a robust monitoring system. 
* Risk of missing early quality drops.

![](<../../../images/2023110\_course\_module4\_fin.048-min.png>)

## Model retraining tradeoffs

The model retraining process isn't just about updating the model. It includes generating and checking the quality of the new dataset, evaluating the model, and updating the service – all of these come with associated costs.

When it comes to retraining, there is always a **tradeoff** between the benefits of improved/sustained model performance and the resources you invest in retraining, such as time, computational and human resources, process automation, and support. 

![](<../../../images/2023110\_course\_module4\_fin.050-min.png>)

## Thinking through the retraining decision

Here are some considerations when deciding whether to retrain the model or not:

**Be pragmatic**. Develop a strategy considering available actions, service properties, resources, model criticality, and the cost of errors. Here is an example of a decision-making logic you can follow: 

![](<../../../images/2023110\_course\_module4\_fin.054-min.png>)

Let’s look at each of the **steps of this decision-making logic** in more detail.

**Check for model performance**. To define whether the model quality has dropped, compare the model performance against a baseline. You should check if the drop is real: it is important to distinguish between the case when the quality dropped for a couple of objects and the case when the quality dropped on top of the whole batch of data.

![](<../../../images/2023110\_course\_module4\_fin.055-min.png>)

**Investigate data quality issues**. If something is wrong with the model, chances are there is something wrong with the data. To investigate potential data quality issues, you can run tests to check for missing values, duplicates, out-of-range values, etc. Remember to **fix the data quality first** and then confirm if retraining is needed. 

![](<../../../images/2023110\_course\_module4\_fin.056-min.png>)

**Investigate data drift**. If the data quality is OK, it can be the data shifts that cause model performance issues. To detect them, check for distribution drift in model target behavior and input data.

If there are no shifts in the data, look for **technical bugs**. If you detect data drift, consider both **retraining** and **switching to alternatives** – rule-based systems, other models, or manual processes. 

![](<../../../images/2023110\_course\_module4\_fin.057-min.png>)

**Decide on retraining if sufficient data is available**. Sometimes, you may have sufficient data to detect drift but not enough to retrain the model. It is useful to come up with a heuristic to define the minimum volume of data you need to retrain the model. 

![](<../../../images/2023110\_course\_module4\_fin.058-min.png>)

**Check your alternatives**. You can consider switching to an alternative decision-making process, like the previous model version, manual processing, non-ML models, or use heuristics.

![](<../../../images/2023110\_course\_module4\_fin.059-min.png>)

**Evaluate model quality before rollout**. You can compare how your alternatives perform on a "golden dataset" which:
* Contains all relevant segments/classes,
* Includes known corner cases or test scenarios,
* Represents the long-term trends, not only recent data.

**The golden dataset should be curated** to reflect assumptions about the data and incorporate domain knowledge. 

![](<../../../images/2023110\_course\_module4\_fin.060-min.png>)

## Summing up

We discussed two main strategies for model retraining: scheduled retraining and trigger-based retraining. Scheduled retraining is a good enough approach but rarely optimal, as you might miss the true decay or waste resources.

How to do better:
* Make sure you evaluate the models before roll-out. 
* Monitor the production model quality and data.
* Test your retraining strategy on historical data to make informed choices.
* Tune and automate retraining the approach, but keep the human in the loop. 

Further reading: [To retrain, or not to retrain? Let's get analytical about ML model updates](https://www.evidentlyai.com/blog/retrain-or-not-retrain)

Up next: we will discuss how to create and curate a reference dataset. 
