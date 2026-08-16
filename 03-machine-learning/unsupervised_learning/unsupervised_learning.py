import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import linkage, dendrogram

X, _ = make_blobs(n_samples=300, centers=5, cluster_std=2, random_state=42)

plt.figure()
plt.scatter(X[:, 0], X[:, 1], s = 50, alpha=0.7, edgecolors="k")
plt.title("Ham veri")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
kmeans.fit(X)

labels = kmeans.labels_
print(labels)

plt.figure()
plt.scatter(X[:, 0], X[:, 1], s = 50, c = labels, cmap = "viridis", alpha=0.7, edgecolors="k")

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], s = 150, c = "red", marker = "X", label= "centroid")
plt.title("K-Means Kümeleme")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()


agg = AgglomerativeClustering(n_clusters=4, linkage="ward")
agg_labels = agg.fit_predict(X)


plt.figure()
plt.scatter(X[:, 0], X[:, 1], s = 50, c = agg_labels, cmap = "viridis", alpha=0.7, edgecolors="k")
plt.title("Agglomerative Kümeleme")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

linked = linkage(X, method="ward")
plt.figure()
dendrogram(linked)
plt.title("Dendrogram")
plt.xlabel("Veri noktaları")
plt.ylabel("Uzaklık")
plt.show()