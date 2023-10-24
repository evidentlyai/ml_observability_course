# 3.6. Monitoring multimodal datasets

{% embed url="https://www.youtube.com/watch?v=b0a1iMlHgEs&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=20" %}

**Video 6**. [Monitoring multimodal datasets](https://www.youtube.com/watch?v=b0a1iMlHgEs&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=20), by Emeli Dral

## What is a multimodal dataset?

Often, we don't only work with structured or unstructured data but a combination of both. Some common examples include product reviews, chats, support tickets, and emails. These applications may include unstructured data, e.g., text, and structured metadata like the region, device, product type, user category, etc.

Both structured and unstructured data provide valuable signals. Considering signals from both data types is essential to build comprehensive ML models.

![](<../../../images/2023109\_course\_module3.044-min.png>)

## Monitoring strategies for multi-modal data

We will cover three widely used strategies for monitoring multi-modal datasets. 

**Strategy 1. Split and monitor independently.**
The approach is straightforward – split the dataset by data type and monitor structured and unstructured data independently:
* Monitor structured data using descriptive statistics, share of missing values, distribution drift, correlation changes, etc. 
* Use raw text data analysis or embedding monitoring for unstructured data. 
* Combine monitoring results into a unified dashboard.

![](<../../../images/2023109\_course\_module3.046-min.png>)

**Strategy 2. A joint structured dataset.**
This approach is based on turning unstructured data into structured by using descriptors:
* Generate descriptors for unstructured data (e.g., text properties) to represent it in a structured form. 
* Combine these structured descriptors with existing metadata. 
* Perform a comprehensive analysis of the combined structured data. You can check for missing values, distribution drift, correlation changes, outliers, etc.

![](<../../../images/2023109\_course\_module3.047-min.png>)

**Strategy 3. Generate embeddings.** 
As embeddings represent data as vectors in high-dimensional space, you can combine structured features with embeddings to create an expanded feature space. For instance, if you have 64 embeddings and three structured features, the combined space would be 67-dimensional. You can then apply various methods like share of drifted components, domain classifier, or distance-based metrics to this combined data.

![](<../../../images/2023109\_course\_module3.048-min.png>)

## Summing up

We discussed three strategies for monitoring data quality and data drift in multi-modal datasets. This concludes our module on ML monitoring for unstructured data. Here are some considerations to keep in mind:
* **If you have access to raw text data, do not ignore it.** Interpretability wins! Evaluating metrics on raw text can provide a deep understanding of changes and potential issues with text data.
* **If working with embeddings,** numerous methods are also available to detect drift.
* **When dealing with multimodal datasets,** you can split data by type, leverage text descriptors, or generate a joint embedding dataset, depending on the specific use case and available data.

