---
description: What text descriptors are and how to use them to monitor text data quality and data drift.
---

# 3.3. Monitoring text data quality and data drift with descriptors

{% embed url="https://www.youtube.com/watch?v=UwWGxyCHQSw&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=17" %}

**Video 3**. [Monitoring text data quality and data drift with descriptors](https://www.youtube.com/watch?v=UwWGxyCHQSw&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=17), by Emeli Dral

## What is a text descriptor?

A **text descriptor** is any feature you can derive or calculate from raw text. Text descriptor transforms unstructured data (e.g., text) into structured data (e.g., numeric or categorical descriptors). 

Depending on your goal and problem statement, there are various groups of descriptors you can calculate:
* **Text data quality.** Example descriptors are text length, the share of out-of-vocabulary words, the share of non-letter characters, regular expressions match, etc.

![](<../../../images/2023109\_course\_module3.024-min.png>)

* **Text contents.** For instance, you can monitor the presence of trigger words like mentions of specific brands or competitors or text sentiment. Collaborating with product managers or business teams is recommended to determine the meaningful text descriptors for your problem statement and domain area.

![](<../../../images/2023109\_course\_module3.025-min.png>)

You can also use **LLM-based grading** that replicates the evaluation that human assessors can do. In this scenario, you automate evaluations by using an LLM to “judge” the generated outputs.

For example, it can assign a score, check whether the text answers a specific question, define the tone of the output, etc. This method has its caveats: it is not always reliable, can be costly, and requires another set of prompts and outputs to monitor.

![](<../../../images/2023109\_course\_module3.026-min.png>)

{% hint style="info" %}
**Further reading:** [Monitoring unstructured data for LLM and NLP with text descriptors](https://www.evidentlyai.com/blog/unstructured-data-monitoring).
{% endhint %}

## Monitoring text descriptors

Once you have a structured representation of the unstructured data – in our case, text descriptors – you can use monitoring techniques applied to structured data. For example, you can:
* Measure **descriptor distribution drift**.
* Run **rule-based checks**, such as min-max ranges for text length, the expected share of non-letter symbols, or responses that match a regular expression.
* Track any **statistics calculable for tabular data**, e.g., correlation changes between descriptors and model target.

![](<../../../images/2023109\_course\_module3.029-min.png>)

## Summing up

We introduced basic concepts and examples of text descriptors. You can calculate myriad descriptors, and we recommend collaborating with someone from your business team to determine text descriptors that fit your problem statement best. 

While text descriptors are a powerful tool to analyze and monitor unstructured text data, we can use this approach only if the raw text is available. Other monitoring strategies may be required for scenarios where only embeddings are available.

Further reading: [Monitoring unstructured data for LLM and NLP with text descriptors](https://www.evidentlyai.com/blog/unstructured-data-monitoring)

Up next: monitoring embeddings drift.
