
import tweepy

#max_results per page can be in [5,100]
def get_tweets(user_id, client, num_tweets=10, max_results_per_page=5):
    pages = num_tweets//max_results_per_page
    tweet_text = {}

    response = client.get_users_tweets(user_id, max_results=5, 
            exclude='retweets')
    
    for tweet in response.data:
        tweet_text[tweet.id] = tweet.text

    next_token = response.meta['next_token']

    for i in range(pages-1):
        response = client.get_users_tweets(user_id, max_results=max_results_per_page, 
            exclude='retweets', pagination_token=next_token)
        
        for tweet in response.data:
            tweet_text[tweet.id] = tweet.text
        if ('next_token' not in response.meta):
            break
        next_token = response.meta['next_token']

                
    return tweet_text