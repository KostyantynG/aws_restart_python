import requests
import json

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

