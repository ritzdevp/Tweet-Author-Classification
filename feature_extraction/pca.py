import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import KernelPCA

# Loading data from npz file
feature_data = np.load('../tfidf_features.npz')
tfidf_vectors = feature_data['name1']
user_labels = feature_data['name2']

# Applying Kernel PCA
transform = KernelPCA(n_components = 2, kernel = 'rbf')
feature_data_transformed = transform.fit_transform(tfidf_vectors)

# Applying KMeans 
kmeans = KMeans(n_clusters = 10).fit(feature_data_transformed)
label = kmeans.labels_

# Scatter plot
u_labels = np.unique(label)
for i in u_labels:
    plt.scatter(feature_data_transformed[label == i , 0] , feature_data_transformed[label == i , 1], label = i, s = 8)

plt.legend()
plt.title("Scatter plot after applying KernelPCA and KMeans")
plt.xlabel("Comp 1")
plt.ylabel("Comp 2")
plt.show()
plt.savefig('img.png')
