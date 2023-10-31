import requests
import json
import time

def get_messages():
    while True:
        response = requests.get('http://localhost:5000/get_messages')
        messages = response.json()
        print("Received Messages:")
        for message in messages['messages']:
            print(message)
        time.sleep(1)  # Poll the server every 1 second

if __name__ == '__main__':
    get_messages()
