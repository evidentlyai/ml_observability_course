---
description: A code example walkthrough of creating a live ML monitoring dashboard for online architecture using Evidently.
---

# 6.3. ML model monitoring dashboard with Evidently. Online architecture [CODE PRACTICE]

{% embed url="https://youtu.be/2hTRXEOJF8k?si=CCVRwxiWWyZGmZF7" %}

**Video 3**. [ML model monitoring dashboard with Evidently. Online architecture [CODE PRACTICE]](https://youtu.be/2hTRXEOJF8k?si=CCVRwxiWWyZGmZF7), by Emeli Dral

In this video, we create a live ML monitoring dashboard for an ML model deployed as a service. We imitate sending the live data directly from the machine learning service to the ML monitoring service and update the dashboard in near real-time.

**Want to go straight to code?** Here is the [code example](https://github.com/evidentlyai/ml_observability_course/blob/main/module6/online_monitoring_dashboard.py) to follow along.

**Outline:** \
[00:00](https://www.youtube.com/watch?v=2hTRXEOJF8k&t=0s) Introduction \
[00:30](https://www.youtube.com/watch?v=2hTRXEOJF8k&t=30s) Script overview and imports \
[01:59](https://www.youtube.com/watch?v=2hTRXEOJF8k&t=119s) Define Collector, Workspace, and Project variables \
[03:31](https://www.youtube.com/watch?v=2hTRXEOJF8k&t=211s) Load data and create mini-batches to simulate production usage \
[04:39](https://www.youtube.com/watch?v=2hTRXEOJF8k&t=279s) Implement the function to generate Test Suites \
[06:38](https://www.youtube.com/watch?v=2hTRXEOJF8k&t=398s) Create the Workspace, Project and add Dashboard panels \
[09:25](https://www.youtube.com/watch?v=2hTRXEOJF8k&t=565s) Set up and configure the Collector service \
[13:00](https://www.youtube.com/watch?v=2hTRXEOJF8k&t=780s) Simulate sending data to the Collector \
[15:48](https://www.youtube.com/watch?v=2hTRXEOJF8k&t=948s) Implement the main function, run and debug the script \
[18:32](https://www.youtube.com/watch?v=2hTRXEOJF8k&t=1112s) Run the Collector and view the online Dashboard updates \
[20:46](https://www.youtube.com/watch?v=2hTRXEOJF8k&t=1246s) Recap and next steps
