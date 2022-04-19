import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


# df = pd.read_csv('../data.csv', index_col=[0])

# all_tweets_list = df['tweet'].to_list()

# vectorizer = TfidfVectorizer()
# vectors = vectorizer.fit_transform(all_tweets_list[:5])
# words = vectorizer.get_feature_names()
# tfidf_list = vectors.todense().tolist()
# df = pd.DataFrame(tfidf_list, columns=words)
# print(tfidf_list)
# print(words)

def get_tfidf_list(tweets_list_df, vocab):
    vectorizer = TfidfVectorizer(vocabulary=vocab)
    vectors = vectorizer.fit_transform(tweets_list_df.values.astype('U'))
    words = vectorizer.get_feature_names()
    tfidf_list = vectors.todense().tolist()
    return tfidf_list
    # df = pd.DataFrame(tfidf_list, columns=words)
    # print(tfidf_list)
    # print(words)


# tf_x_train = vectorizer.fit_transform(X_train)
# tf_x_test = vectorizer.transform(X_test)