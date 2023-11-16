---
description: Types of custom metrics. Business or product metrics, domain-specific metrics, and weighted metrics.
---

# 4.5. Custom metrics in ML monitoring

{% embed url="https://youtu.be/PrFuzKLM66I?si=68EF7tepIyXxyMig" %}

**Video 5**. [Custom metrics in ML monitoring](https://youtu.be/PrFuzKLM66I?si=68EF7tepIyXxyMig), by Emeli Dral

## Types of custom metrics

While there is no strict division between “standard” and “custom” metrics, there is some consensus on evaluating, for example, classification model quality using metrics like precision and recall. They are fairly “standard.”  

However, you often need to implement “custom” metrics to reflect specific aspects of model performance. They typically refer to business objectives or domain requirements and help capture the impact of an ML model within its operational context.

Here are some examples. 

**Business and product KPIs (or proxies)**. These metrics are aligned with key performance indicators that reflect the business goals and product performance. 

**Examples include**:
* Manufacturing optimization: raw materials saved.
* Chatbots: number of successful chat completions.
* Fraud detection: number of detected fraud cases over $50,000.
* Recommender systems: share of recommendation blocks without clicks.

We recommend **consulting with business stakeholders** even before building the model. They may suggest valuable KPIs, heuristics, and metrics that could be monitored even during the experimentation phase.

When direct measurement of a KPI is not possible, consider **approximating the model impact**. For example, you can assign an average “cost” to specific types of model errors based on domain knowledge.

![](<../../../images/2023110\_course\_module4\_fin.078-min.png>)

**Domain-specific ML metrics**. These are metrics that are commonly used in specific domains and industries. 

**Examples include**:
* Churn prediction in telecommunications: lift metrics.
* Recommender systems: serendipity or novelty metrics.
* Healthcare: fairness metrics.
* Speech recognition: word error rate.
* Medical imaging: Jaccard index.

![](<../../../images/2023110\_course\_module4\_fin.079-min.png>)

**Weighted or aggregated metrics**. Sometimes, you can design custom metrics as a “weighted” variation of other metrics. For example, you can adjust them to account for the importance of certain features or classes in your data. 

**Examples include**:
* Data drift weighted by feature importance.
* Measuring specific recommender system biases, for example, based on product popularity, price, or product group.
* In unbalanced classification problems, you can weigh precision and recall by class or by specific important user groups, such as based on the estimated user Lifetime Value (LTV).

![](<../../../images/2023110\_course\_module4\_fin.080-min.png>)

## Summing up

There is no need to invent “custom” metrics just for the sake of it. However, you might want to implement them to:
* better reflect important model qualities,
* estimate the business impact of the model,
* add metrics useful for product and business stakeholders and accepted within the domain. 

Up next: optional code practice to create and implement a custom quality metric in the Evidently Python library.
