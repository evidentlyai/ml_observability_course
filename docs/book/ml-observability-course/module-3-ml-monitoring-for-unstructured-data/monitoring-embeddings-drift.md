# 3.4. Monitoring embeddings drift

{% embed url="https://www.youtube.com/watch?v=0XtABbNYU7U&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=18" %}

**Video 4**. [Monitoring embeddings drift](https://www.youtube.com/watch?v=0XtABbNYU7U&list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF&index=18), by Emeli Dral

## What are embeddings?

Embeddings are numerical representations of the input data. They transform raw data like text, images, videos, or music into numerical vectors in high-dimensional space. Embeddings are frequently used in machine learning for classification, regression, and ranking tasks with unstructured data.

![](<../../../images/2023109\_course\_module3.032-min.png>)

## Embedding drift detection methods

Since embeddings are numerical values, we can use many methods to monitor embedding distribution drift. 

**Distance metrics**
Each object in the dataset, represented as an embedding, is a numerical vector. Distance metrics allow calculating distances between these vectors. For example, you can use Euclidean distance or Cosine distance (to assess the angle between vectors). We can detect shifts in datasets by measuring the distance between centroids of reference data and current data.

![](<../../../images/2023109\_course\_module3.035-min.png>)

**Model-based drift detection**
This approach uses embeddings to build a domain classifier that distinguishes between reference and current data. The idea is similar to model-based drift detection on raw text data: you get an estimation of the model's ability to distinguish between datasets. However, with embeddings, this approach has a limitation: you cannot use the information about the strongest features or best objects to determine the root cause/source of drift.

![](<../../../images/2023109\_course\_module3.036-min.png>)

**Share of drifted components**
You can also use the share of drifted components to monitor embedding drift. This approach treats each embedding component independently and uses drift detection methods that can be applied to numerical values. For each component, drift size or score is assessed. You can then aggregate these individual scores into the number of drifted components or share of drifted components. 

![](<../../../images/2023109\_course\_module3.037-min.png>)

{% hint style="info" %}
**Further reading:** [Shift happens: we compared 5 methods to detect drift in ML embeddings](https://www.evidentlyai.com/blog/embedding-drift-detection).
{% endhint %}

The suggested blog might be especially interesting to those who work a lot of embeddings. It compares various methods to detect drift in embeddings – Euclidean distance, Cosine distance, Domain classifier, Share of drifted components, and Maximum mean discrepancy (MMD) – and evaluates each method against such criteria as computational speed, thresholds, PCA, and embedding model behavior. 

Domain classifier can be a good default: it is comparably fast, PCA-agnostic, agnostic to the embedding model, and easy to interpret. However, we suggest you check out the blog to choose the right drift detection method for your specific use case. Here is a blog summary sneak peek:

![](<../../../images/2023109\_course\_module3.039-min.png>)

## Summing up

We discussed different strategies for monitoring embedding drift, including distance metrics, model-based drift detection, and share of drifted components. While using a domain classifier to detect embedding drift is a good default strategy, we suggest you evaluate other methods to choose the right one for your use case. 

Up-next: code practice! We will apply ML monitoring strategies for unstructured data on real data to derive actionable metrics. 
