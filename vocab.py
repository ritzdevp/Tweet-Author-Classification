import numpy as np
import pandas as pd
from collections import Counter
import string
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv('cleaned_tweets.csv', index_col=[0])
df.columns = ['tweet', 'user']

all_tweets_list = df['tweet']

# print(all_tweets_list[7000].split("\\s"))
# print('hello 123'.split("\\s"))

word_sep = []
count = 0
i = 0
for t in all_tweets_list:
    # print(t)
    try:
        word_sep += t.split()
    except:
        # print(i,t)
        count += 1
    i += 1

# print(all_tweets_list[36915])
print("Nan count = ", count)

print(len(word_sep))

dummy = [
    ['hello', 'world'],
    ['why', 'hello', 'world'],
    ['come', 'back', 'world']
]

# print(word_sep.count())
print(len(Counter(word_sep)))

count_dict = Counter(word_sep)

count_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True) 
print(count_list[:5]) 

rare = 0
for item in count_list:
    if (item[1] < 10):
        rare+=1

print(count_list[0])
vocab = []
dump = ["—", "...", "”", "“", "\n", "🇸", "🇺", "..", ]

single_chars = string.ascii_lowercase + string.digits

for ch in single_chars:
    dump.append(ch)

for w in count_list[:-rare]:
    if (w[0] in dump):
        continue
    vocab.append(w[0])


vocab_np = np.array(vocab)
np.savetxt('vocab.txt', vocab_np, fmt='%s')

print('vocab len ', len(vocab))
print(len(count_list)-rare)
# print(len(count_list))
print(rare)
print('rare % ', rare/len(count_list) * 100)