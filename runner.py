import os
import dotenv
import json
import tweepy
import user_ids
import tweet_retrieve
from dotenv import load_dotenv
load_dotenv()

bearer_token = os.getenv('BEARER_TOKEN')
client = tweepy.Client(bearer_token)

num_tweets = 2800
max_results_per_page = 100

data = {}

for user in user_ids.users:
    retrieved_tweets = tweet_retrieve.get_tweets(
        user_ids.users[user],client,
        num_tweets, max_results_per_page)
    
    data[user] = retrieved_tweets


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)