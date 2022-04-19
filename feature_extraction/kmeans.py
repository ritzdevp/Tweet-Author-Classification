import numpy as np
import pandas as pd

feature_data = np.load('../tfidf_features.npz')

tfidf_vectors = feature_data['name1']
user_labels = feature_data['name2']

print(len(tfidf_vectors))
print(len(user_labels))