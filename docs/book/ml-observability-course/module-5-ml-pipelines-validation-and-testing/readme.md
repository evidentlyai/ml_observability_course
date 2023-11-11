---
description: This code-focused module demonstrates how to deploy an end-to-end pipeline for data and ML model quality checks.
---

# Module 5: ML pipelines validation and testing [PRACTICE]

In previous modules, we covered what ML monitoring is, which metrics and tests to use, and what to consider in ML monitoring design. Now, let’s get to practice! This is a code-focused module.

We will apply the learnings and **implement data and model quality tests as part of a pipeline**. If you deal with batch models, such test-based monitoring can often cover all your needs. For online models, this can be a part of your setup. You can run batch checks when you get labeled data or retain the models.

We will go through an **end-to-end pipeline using a toy dataset**. We will train a model and design tests for data and model quality using Evidently. We will also explore how to automate the data pipeline testing using tools like Airflow, Prefect, and Mlflow. 
