import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from collections import Counter
import random
import matplotlib.pyplot as plt

def helper(counter_object):
  temp = {}
  for k,v in counter_object.items():
    temp[k] = v
  return temp

feature_data = np.load('../tfidf_features.npz')

tfidf_vectors = feature_data['name1']
# user_labels = feature_data['name2']

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
user_labels = df['user']

cluster_tweets = []
cluster_users = []

for i in range(n_clusters):
    cluster_tweets.append([])
    cluster_users.append([])

for i in range(len(all_tweets_list)):
    cluster_label = clusters[i]
    cluster_tweets[cluster_label].append(all_tweets_list[i])
    cluster_users[cluster_label].append(user_labels[i])


histo_list = []
for i in range(len(cluster_tweets)):
    print("CLUSTER ", i)
    print("=========\n")
    ct = cluster_tweets[i].copy()
    random.shuffle(ct)
    for j in range(20):
        print(ct[j])
    
    x = Counter(cluster_users[i])
    histo_list.append(helper(x))
    print(x)

print(histo_list[0].keys())
print(histo_list[0].values())
print(type(list(histo_list[0].values())[0]))
plt.bar(list(histo_list[0].keys()), list(histo_list[0].values()), color='g')
plt.savefig('visualize.jpeg')