import json
import boto3

s3_client = boto3.client('s3')

def upload_joke(joke_json):
    with open('joke.json', 'w') as file:
        file.write(json.dumps(joke_json))

    s3_client.upload_file('joke.json', 'bucket-for-my-boto-stuff', 'joke.json')