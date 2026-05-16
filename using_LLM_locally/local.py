from langchain.chat_models import init_chat_model


model = init_chat_model(
    model="phi3:mini",
    model_provider="ollama"
)

response = model.invoke("Is learnng Python in a year possible?")
print(response.text)
