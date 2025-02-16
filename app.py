"""
Documentation :
https://ai.google.dev/gemini-api/docs/text-generation?lang=python

"""

from dotenv import load_dotenv

load_dotenv()  ## loading all the environment variables

import streamlit as st
import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL_ID = "gemini-2.0-flash"

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
# This is to store the chat history of all conversations in a format that Google API requires
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

## function to load Gemini Pro model and get repsonses
chat = client.chats.create(model=MODEL_ID, history=st.session_state["chat_history"])

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input:
    response = chat.send_message(input)
    # Add user query and response to session state chat_history - For passing as history parameter to the chat session
    st.session_state["chat_history"].extend(
        [
            types.Content(parts=[types.Part(text=input)], role="user"),
            types.Content(parts=[types.Part(text=response.text)], role="model"),
        ]
    )

    # Print the response
    st.subheader("The Response is")
    st.write(response.text)


# Printing chat history
st.subheader("The Chat History is")
for message in st.session_state["chat_history"]:
    st.write(f"{message.role.upper()} : {message.parts[0].text}")
