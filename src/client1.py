import requests
import json

def send_message(message):
    data = {'message': message}
    response = requests.post('http://localhost:5000/send_message', json=data)
    return response.json()

if __name__ == '__main__':
    while True:
        message = input("Enter a message to send: ")
        response = send_message(message)
        print(response)
        
