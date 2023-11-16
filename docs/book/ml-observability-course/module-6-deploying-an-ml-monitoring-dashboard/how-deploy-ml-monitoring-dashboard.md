---
description: ML monitoring architectures recap and how to deploy a live ML monitoring dashboard.
---

# 6.1. How to deploy a live ML monitoring dashboard

{% embed url="https://youtu.be/AZxp7f5IahU?si=JE-rf1g6iHoHSipU" %}

**Video 1**. [How to deploy a live ML monitoring dashboard](https://youtu.be/AZxp7f5IahU?si=JE-rf1g6iHoHSipU), by Emeli Dral

## Why build a monitoring dashboard? 

Tests and reports are great for running structured checks and exploring and debugging your data and ML models. However, when you run tests or build an ad-hoc report, you evaluate only a **specific batch of data**. This makes your monitoring **“static”**: you can get alerts but have no visibility into metric evolution and trends. 

That is where the ML monitoring dashboard comes into play, as it:
* Tracks metrics over time,
* Aids in trend analysis and provides insights,
* Provides a shared UI to enhance visibility for stakeholders, e.g., data scientists, model users, product managers, business stakeholders, etc.

![](<../../../images/202310\_module6.004-min.png>)

## ML monitoring architectures recap

Before proceeding to the code practice of building a monitoring dashboard, let’s quickly recap ML monitoring architectures and how they differ. 

ML monitoring starts with **logging**. To set up an effective ML monitoring backend for your service, you need to log input data, model outputs, and labeled data (if available) – they can be recorded in a **prediction store**.

You can send logged data to an **ML monitoring service** or run **monitoring jobs** to calculate monitoring metrics. Both methods allow recording calculated metrics in a **metric store**, which you can use as a data source to build a **monitoring dashboard**.

![](<../../../images/202310\_module6.006-min.png>)

## Code practice overview

We will show how to design and deploy an ML monitoring dashboard for batch and near real-time model monitoring architectures. 

**For batch monitoring**, we will use Evidently open-source ML monitoring architecture. We will:
* Create **snapshots** that are individual Reports or Test Suites computed for a specific period (e.g., hour, day, week) in a rich JSON format.
* Log them to a file system and run an ML monitoring service that reads data from snapshots.
* Design dashboard panels and visualize **data and model metrics over time**. You can easily switch between time-series data and individual Reports/Test Suites for further analysis and debugging. 

![](<../../../images/202310\_module6.010-min.png>)

**For near real-time monitoring**, Evidently provides a **collector service**:
* It collects incoming data and computes Reports / Test Suites continuously.
* You can configure the service to calculate snapshots over various time intervals (as opposed to writing batch jobs on your own – you can define the frequency of batches using a config file).
* The service outputs the same snapshots as in the batch monitoring scheme: the front-end is the same.

![](<../../../images/202310\_module6.014-min.png>)

We will also cover an **alternative architecture using Grafana**, a popular open-source visualization tool. We will walk you through the Evidently and Grafana integration example – you can parse data computed by Evidently, store it in a chosen database, and visualize it in Grafana. In this case, Evidently serves as an evaluation layer.

This can be a good alternative if you already use Grafana for monitoring and alerting for other services.  

And now, to practice!
