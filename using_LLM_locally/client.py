
import requests

API_URL = "http://localhost:5009"
url = f"{API_URL}/chat"

history = []

while True:
    user_input = input("You question: ")
    history.append({"role": "user", "content": user_input}
                   
                   )
    response = requests.post(url, json={"inputs": history})

    assistant_message = response.json()['message']
    history.append(assistant_message)
    print(assistant_message['content'])