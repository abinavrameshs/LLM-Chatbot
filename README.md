# LLM-Chatbot

Application on Streamlit to chat with an LLM.
Here we use the LLM `gemini-2.0-flash`.
We can also alternatively use any other LLM as well. This code will work with Google APIs

## Setup

This project is initialized using `pdm`. To learn more about `pdm` please refer to [pdm documentation](https://pdm-project.org/en/latest/)

- Install `pdm` using the command: `pip install pdm`
- Then initialize a blank project using the command `pdm init`. This will provide a bunch of prompts to fill, after which a template is created for you.


## Requirements

We require 3 libraries to run this project
- `streamlit`: For creating our frontend application
- `google-genai`: For using Google's LLMs (Like Google Pro, Google Flash models)
- `python-dotenv`: Used to load `.env` files

- You will have to create a `.env` file in the root of your repo and include the following

`GOOGLE_API_KEY = <YOUR_API_KEY>`

## Executing the project

- After installing the required packages, run `pdm run streamlit run app.py` to run the streamlit Chatbot app with conversation history

## Demo of the Project

![](https://github.com/abinavrameshs/LLM-Chatbot/blob/main/docs/Cropped%20demo.gif)


## References

- [Google API Docs](https://ai.google.dev/gemini-api/docs/document-processing?lang=python)