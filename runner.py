import os
import dotenv
import tweepy
import user_ids
import tweet_retrieve
from dotenv import load_dotenv
load_dotenv()

bearer_token = os.getenv('BEARER_TOKEN')
client = tweepy.Client(bearer_token)

print(user_ids.users)