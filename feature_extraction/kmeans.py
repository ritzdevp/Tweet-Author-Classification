import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from collections import Counter

feature_data = np.load('../tfidf_features.npz')

tfidf_vectors = feature_data['name1']
user_labels = feature_data['name2']

n_clusters = 5
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(tfidf_vectors)

#labels assigned to each tweet
clusters = kmeans.labels_
print("len = ", len(clusters))
counts = Counter(clusters)
print(counts)

df = pd.read_csv('../cleaned_tweets.csv', index_col=[0])
print("df len", len(df))
df.columns = ['tweet', 'user']

all_tweets_list = df['tweet']

cluster_tweets = []
for i in range(n_clusters):
    cluster_tweets.append([])

for i in range(len(all_tweets_list)):
    cluster_label = clusters[i]
    cluster_tweets[cluster_label].append(all_tweets_list[i])


for i in range(len(cluster_tweets)):
    print("CLUSTER ", i)
    print("=========\n")
    for j in range(10):
        print(cluster_tweets[i][j])