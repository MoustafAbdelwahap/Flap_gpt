import openai
import streamlit as st
import requests

import streamlit as st
import ChatGPTAPIFree

# Get the ChatGPT API key
api_key = st.config.get("chatgpt_api_key")

# Create a ChatGPTAPI object
chatgpt = ChatGPTAPIFree.ChatGPTAPI(api_key)

# Define a function to generate text from the ChatGPT API
def generate_text(prompt):
  response = chatgpt.generate_text(prompt)
  return response["text"]

# Create a text input field for the user to enter a prompt
prompt = st.text_input("Prompt:")

# Generate text from the prompt
generated_text = generate_text(prompt)

# Display the generated text to the user
st.markdown(generated_text)

