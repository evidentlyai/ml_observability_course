---
description: A code example walkthrough of adding ML monitoring metrics to Grafana using Evidently as an evaluation layer.
---

# 6.4. ML monitoring with Evidently and Grafana [OPTIONAL CODE PRACTICE]

{% embed url="https://youtu.be/S4zFqbLhAp8?si=BEfLZteDmj94XPpD" %}

**Video 4**. [ML monitoring with Evidently and Grafana [OPTIONAL CODE PRACTICE]](https://youtu.be/S4zFqbLhAp8?si=BEfLZteDmj94XPpD), by Emeli Dral

In this video, we show how to add ML monitoring metrics to the Grafana dashboard using Evidently as an evaluation layer and storing the metrics in a Postgres database.

**Want to go straight to code?** Here is the [code example](https://github.com/evidentlyai/ml_observability_course/tree/main/module6/grafana_monitoring_dashboard) to follow along.

**Outline:** \
[00:00](https://www.youtube.com/watch?v=S4zFqbLhAp8&t=0s) Introduction \
[00:25](https://www.youtube.com/watch?v=S4zFqbLhAp8&t=25s) Install Grafana and set up the Postgres database \
[03:18](https://www.youtube.com/watch?v=S4zFqbLhAp8&t=198s) Script overview, imports, and logging \
[04:50](https://www.youtube.com/watch?v=S4zFqbLhAp8&t=290s) Create a table statement \
[06:30](https://www.youtube.com/watch?v=S4zFqbLhAp8&t=390s) Load data and simulate production usage \
[07:30](https://www.youtube.com/watch?v=S4zFqbLhAp8&t=450s) Connect to a database and create a table \
[10:32](https://www.youtube.com/watch?v=S4zFqbLhAp8&t=632s) Calculate metrics and insert them into Postgres \
[16:00](https://www.youtube.com/watch?v=S4zFqbLhAp8&t=960s) Write a function to compute metrics in batches \
[18:58](https://www.youtube.com/watch?v=S4zFqbLhAp8&t=1138s) Run services, execute and debug the script \
[23:21](https://www.youtube.com/watch?v=S4zFqbLhAp8&t=1401s) Create dashboards in Grafana
