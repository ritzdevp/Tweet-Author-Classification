import numpy as np
import pandas as pd
from feature_extraction import tfidf

df = pd.read_csv('cleaned_tweets.csv', index_col=[0])
print("df len", len(df))
df.columns = ['tweet', 'user']

all_tweets_list = df['tweet']

vocab = np.loadtxt('vocab.txt', dtype=str)
print(len(vocab))

tfidf_list = tfidf.get_tfidf_list(all_tweets_list, vocab)
# print("len of tfidf_list", len(tfidf_list))
# print(len(tfidf_list[0]))
user_labels = df['user'].tolist()

tfidf_list_np = np.array(tfidf_list)
user_labels_np = np.array(user_labels)
np.savez('tfidf_features.npz', name1=tfidf_list_np, name2=user_labels_np)

