import requests

def get_joke():

    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    return {
        "id": data["id"],
        "joke": data["value"],
        }
