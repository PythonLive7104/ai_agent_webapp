from langchain.chat_models import init_chat_model
from flask import Flask, request, jsonify

app = Flask(__name__)

'''
The project involves using LLM models locally, specifically using the Ollama platform to run the gpt-4.1-mini model.
The locally downloaded model is tinyllama, which is a smaller version of the GPT-4 model. The project also involves building an API using Flask and Langchain to interact with the model.

The flask API will have a single endpoint /chat, which will accept POST requests with a JSON payload containing the conversation history. The API will use the Langchain library to invoke the model and generate a response based on the conversation history. The response will be returned as a JSON object containing the assistant's message.
'''

model = init_chat_model(
    model="tinyllama",
    model_provider="ollama"
)
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    response = model.invoke(data["inputs"])

    return jsonify(
        {"message": {
            "role": "assistant",
            "content": response.content
        }}
    )


# response = model.invoke("Is learnng Python in a year possible?")
# print(response.text)


if __name__ == "__main__":
    app.run(debug=True, port=5009) 

