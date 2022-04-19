import numpy as np
from numpy import NaN
import pandas as pd
import csv 
import string
from tqdm import tqdm


import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords


nltk.download('stopwords')

def tokenize(tweet):
    lemmatizer = nltk.stem.WordNetLemmatizer()
    tokenizer = TweetTokenizer()
    return [(lemmatizer.lemmatize(ele)) for ele in tokenizer.tokenize(tweet)]

def pp():
    df_data = pd.read_csv('data.csv')

    # All tweets
    tweet_list = df_data["tweet"].tolist()
    author = df_data["user"].tolist()
    
    tokenized_tweets = []
    for i in tqdm(range(len(tweet_list))):
        if(tweet_list[i] is not NaN):
            tokenized_tweets.append(tokenize(tweet_list[i]))

    for i in tqdm(range(len(tokenized_tweets))):
        tokenized_tweets[i] = [ele.lower() for ele in tokenized_tweets[i] if(not(ele.startswith("@") \
                                                                    or ele.startswith("https") \
                                                                    or ele.lower() in stopwords.words('english') \
                                                                    or ele in string.punctuation + '’‘।…'))]

    cleaned_data = list(zip(tokenized_tweets, author))
    np.save("cleaned_data.npy", cleaned_data)
    for i in range(10):
        print(cleaned_data[i])


def main():
    pp()

if __name__ == "__main__":
    main()