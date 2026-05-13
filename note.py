'''
For this project, we will be using lagchain package. langchain is a framework for developing applications 
    powered by language models. It provides a standard interface for all LLMs, as well as tools and 
    integrations to make it easy to build applications that use them. 

In this project, we will be using the following components of langchain:
    - LLMs: We will be using the OpenAI GPT-3.5-turbo model to generate responses to user queries.
    - Prompts: We will be using prompts to guide the LLM in generating responses. We will be using a few 
        different prompts to handle different types of queries.
    - Chains: We will be using chains to combine multiple prompts and LLM calls together to create more complex 
        applications. For example, we will be using a chain to first generate a response to a user query, and 
        then use that response to generate a follow-up question.
    - Agents: We will be using agents to create more complex applications that can interact with the user and 
        perform actions based on the user's input. For example, we will be using an agent to create a simple 
        chatbot that can answer

For langchain to connect AI LLMs, we need a module:
    >> pip install langchain-google-genai
    This module provides a connector to Google's Generative AI models, allowing us to use them in our langchain 
    applications. To get google ai studio API key, follow these steps:
    1. Go to the Google Cloud Console: https://console.cloud.google.com/
    2. Create a new project or select an existing project.
    3. Navigate to the "APIs & Services" section and click on "Credentials".
    4. Click on "Create Credentials" and select "API Key".
    5. Copy the generated API key and keep it secure. You will need this key to authenticate your requests to the Google AI Studio API.

    GOOGLE_API_KEY = 'AIzaSyCHALBMK_9Aw0x7Hml604EKH-0CpIfOuuU'
    name = 'langchain_project'
    project_name = 'projects/538090187478'
    project number = 538090187478

    
Building an AI Agent:
    An AI agent is a software program that can perform tasks autonomously, using artificial intelligence 
    techniques. In this project, we will be building a simple AI agent that can answer questions about 
    different types of wood and their suitability for making furniture.

    To build our AI agent, we will follow these steps:
    1. Define the task: We want our AI agent to be able to answer questions about different types of wood 
        and their suitability for making furniture. 
    2. Collect data: We will collect data about different types of wood and their properties, such as hardness, 
        durability, and appearance. 
    3. Train the model: We will use the collected data to train a language model that can generate responses 
        to user queries about wood.
    4. Create the agent: We will create an agent that can take user input, generate a response using the 
        trained model, and return the response to the user.

    Functions are referred to as tools in langchain. We can create a function that provides information about 
    the weather in a given location, and then use that function as a tool in our agent to answer questions 
    about the weather in different locations. 

    A system prompt is a special type of prompt that provides instructions to the LLM about how to behave. 
    For example, we can use a system prompt to tell the LLM that it is a helpful assistant, and that it 
    should provide accurate and concise answers to user queries. This can help guide the LLM in generating 
    responses that are more relevant and useful to the user. 

'''