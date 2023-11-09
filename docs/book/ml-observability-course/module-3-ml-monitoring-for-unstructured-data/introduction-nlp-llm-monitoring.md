---
description: How to evaluate model quality for NLP and LLMs and monitor text data without labels using raw data, embeddings, and descriptors.
---

# 3.1. Introduction to NLP and LLM monitoring

{% embed url="https://www.youtube.com/watch?v=tYA0h3mPeZE&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=15" %}

**Video 1**. [Introduction to NLP and LLM monitoring](https://www.youtube.com/watch?v=tYA0h3mPeZE&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=15), by Emeli Dral

## Use cases for NLP and LLM models

NLP and LLM models are widely used for both predictive and generative tasks. 

**Predictive applications** include:
* **Classification tasks**, e.g., spam detection, classification of support tickets, evaluating text sentiment, etc.
* **Search (ranking) tasks** are common in e-commerce website search, content recommendations, etc.
* **Information extraction**, like extracting structured information (names, dates, etc.) from text, etc.

**Generative applications** cover such tasks as translation, summarization, and text generation, e.g., conversational interfaces, article generation, code generation, etc.

Modern ML systems are often a combination of those: e.g., a support chatbot includes a classifier to detect intent and a generative model to produce a text response.

## What can go wrong with NLP and LLMs?

All production ML models need monitoring. NLP and LLM models are no exception. To build our monitoring strategy, we need to understand what can go wrong with the models that run on the unstructured data. 

There are standard issues that apply to both unstructured and tabular data:
* **Technical errors** such as wrong encoding or data processing bugs.
* **Data shifts** like new topics or unexpected usage scenarios.

However, there are also issues specific to working with unstructured data. For example:
* **Model attacks,** e.g., prompt injection and adversarial usage. 
* **Model behavior shift.** For example, if you rely on third-party models, you can face changes in their properties due to retraining.
* **Hallucinations** arise when the model starts to generate factually incorrect or unrelated answers.

![](<../../../images/2023109\_course\_module3.004-min.png>)

## ML monitoring metrics for NLP and LLMs

So, what can you monitor to detect the discussed issues? There are two groups of signals to keep tabs on:

**1. Direct signals.** This group includes standard model quality metrics such as accuracy, precision, and recall – and requires labeled data. 

When dealing with **predictive applications** – e.g., classification or ranking tasks – we typically have a "right" answer. In this case, we can label the data and then compare labels and the model’s outputs to calculate direct quality metrics.

However, for **generative applications** (e.g., translation, text summarization), there is often no single correct answer and many possible "good" responses. If this is the case, relying on labels and standard quality metrics is not always possible. Instead, you can use feedback, human labeling, LLM-based grading, and response validation as proxy signals.

![](<../../../images/2023109\_course\_module3.006-min.png>)

**2. Proxy metrics** help evaluate the model properties. You can look out for data quality, data and prediction drift, or user feedback.

Here are three proxy strategies for unstructured data you can use _(disclaimer: we use text as the main type of unstructured data)_:
* **Monitoring raw text data.** Using analytical methods that process raw texts allows you to catch an interpretable signal and use it for hypothesis formulation and debugging.
* **Monitoring text descriptors.** You can extract signals from raw data and compute metrics based on these structured signals.
* **Monitoring embeddings.** When raw data is not available, the embeddings can be used. You can monitor for changes in the distributions of input and output embeddings.

![](<../../../images/2023109\_course\_module3.007-min.png>)

## Summing up

Monitoring NLP and LLM models differs from monitoring models built on structured data. Both predictive and generative applications have their own monitoring needs, and understanding these differences is crucial for effective model observability. You can use both direct quality metrics and proxy signals to keep tabs on production NLP- and LLM-based systems. 

Up next: delving deeper into detecting raw text data drift.
