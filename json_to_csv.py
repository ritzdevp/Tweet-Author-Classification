import json
import pandas as pd

data = None
with open('data.json') as json_file:
    data = json.load(json_file)
 
    # for user in data:
    #     print(user, " \n num tweets: ", len(data[user]))
    #     print()

    data_list = []
    for user in data:
        for tweet in data[user]:
            temp = [tweet, data[user][tweet], user]
            data_list.append(temp)

    print(len(data_list))
    df = pd.DataFrame(data_list, columns=['tweet_id', 'tweet', 'user'])
    print(len(df))
    df.to_csv('data.csv')

