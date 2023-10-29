# 2.4. Data quality in machine learning

{% embed url="https://www.youtube.com/watch?v=IRbmQGqzVZo&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=10" %}

**Video 4**. [Data quality in machine learning](https://www.youtube.com/watch?v=IRbmQGqzVZo&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=10), by Emeli Dral

## What can go wrong with the input data?

If you have a complex ML system, there are many things that can go wrong with the data. The golden rule is: garbage in, garbage out. We need to make sure that the data we feed our model with is fine. 

Some common data processing issues are:
* **Wrong source**. E.g., a pipeline points to an older version of the table.
* **Lost access**. E.g., permissions are not updated.
* **Bad SQL. Or not SQL**. E.g., a query breaks when a user comes from a different time zone and makes an action “tomorrow."
* **Infrastructure update**. E.g., change in computation based on a dependent library.
* **Broken feature code**. E.g., feature computation breaks at a corner case like a 100% discount. 

Issues can also arise if the data schema changes or data is lost at the source (e.g., broken in-app logging or frozen sensor values). If you have several models interacting with each other, broken upstream models can affect downstream models.

![](<../../../images/2023109\_course\_module2.041-min.png>)

## Data quality metrics and analysis

**Data profiling** is a good starting point for monitoring data quality metrics. Based on the data type, you can come up with basic descriptive statistics for your dataset. For example, for numerical features, you can calculate:
* Min and Max values 
* Quantiles
* Unique values
* Most common values 
* Share of missing values, etc. 

Then, you can visualize and compare statistics and data distributions of the current data batch and reference data to ensure data stability.

![](<../../../images/2023109\_course\_module2.047-min.png>)

When it comes to monitoring data quality, you must define the conditions for alerting. 

**If you do not have reference data, you can set up thresholds manually based on domain knowledge**. “General ML data quality” can include such characteristics as:
* no/low share of missing values
* no duplicate columns/rows
* no constant (or almost constant!) features
* no highly correlated features
* no target leaks (high correlation between feature and target)
* no range violations (based on the feature context, e.g., negative age or sales). 

Since setting up these conditions manually can be tedious, it often helps to have a reference dataset. 

**If you have reference data, you can compare it with the current data and autogenerate test conditions based on the reference**. For example, based on the training or past batch, you can monitor for:
* expected data schema and column types
* expected data completeness (e.g., 90% non-empty)
* expected batch size (e.g., number of rows)
* expected patterns for specific columns, such as:
  * non-unique (features) or unique (IDs)
  * specific data distribution types (e.g., normality)
  * expected ranges based on observed values
  * descriptive statistics: averages, median, quantiles, min-max (point estimation or statistical tests with a confidence interval).

## Summing up

Monitoring data quality is critical to ensuring that ML models function reliably in production. Depending on the availability of reference data, you can manually set up thresholds based on domain knowledge or automatically generate test conditions based on the reference.

Up next: hands-on practice on how to evaluate and test data quality using Python and [Evidently](https://github.com/evidentlyai/evidently) library.
