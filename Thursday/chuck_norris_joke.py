import requests
import json
import boto3
s3 = boto3.resource('s3')


url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
data = response.json()
joke = data["value"]
print(joke)
user_rating = int(input("Please rate the joke: "))

if user_rating > 3:
    joke_data_to_save = {
    "id": data["id"],
    "joke": data["value"],
    "rating": user_rating
    }

    joke_data_as_string = json.dumps(joke_data_to_save)

    with open(joke_data_to_save["id"]+'.json', 'w') as f:
        f.write(joke_data_as_string)

    s3.meta.client.upload_file(joke_data_to_save["id"]+'.json', 'bucket-for-my-boto-stuff', joke_data_to_save["id"]+'.json')
