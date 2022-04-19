import json

data = None
with open('data.json') as json_file:
    data = json.load(json_file)
    count = 0
    for user in data:
        print(user, " \n num tweets: ", len(data[user]))
        count+= len(data[user])
        print()

    print(count)