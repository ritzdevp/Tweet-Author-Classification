import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def get_tfidf_list(tweets_list_df, vocab):
    vectorizer = TfidfVectorizer(vocabulary=vocab)
    vectors = vectorizer.fit_transform(tweets_list_df.values.astype('U'))
    words = vectorizer.get_feature_names()
    tfidf_list = vectors.todense().tolist()
    return tfidf_list
    
# tf_x_train = vectorizer.fit_transform(X_train)
# tf_x_test = vectorizer.transform(X_test)