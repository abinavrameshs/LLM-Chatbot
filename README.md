# LLM-Chatbot

Application on Streamlit to chat with an LLM. Here we use the LLM `gemini-2.0-flash`. We can also alternatively use any other LLM as well. This code will work with Google APIs.

## Table of Contents

- [Setup](#setup)
- [Requirements](#requirements)
- [Executing the Project](#executing-the-project)
- [Demo of the Project](#demo-of-the-project)
- [References](#references)
- [Contributing](#contributing)
- [License](#license)

## Setup

This project is initialized using `pdm`. To learn more about `pdm` please refer to [pdm documentation](https://pdm-project.org/en/latest/).

1. Install `pdm` using the command:
    ```sh
    pip install pdm
    ```
2. Initialize a blank project using the command:
    ```sh
    pdm init
    ```
    This will provide a bunch of prompts to fill, after which a template is created for you.

## Requirements

We require 3 libraries to run this project:

- [streamlit](http://_vscodecontentref_/3): For creating our frontend application
- [google-genai](http://_vscodecontentref_/4): For using Google's LLMs (Like Google Pro, Google Flash models)
- `python-dotenv`: Used to load [.env](http://_vscodecontentref_/5) files

You will have to create a [.env](http://_vscodecontentref_/6) file in the root of your repo and include the following:

```env
GOOGLE_API_KEY = <YOUR_API_KEY>
```

## Executing the project

After the required packages, run the following command to start the Streamlit Chatbot app with conversation history:

```python
pdm run streamlit run app.py
```

## Demo of the Project

![](https://github.com/abinavrameshs/LLM-Chatbot/blob/main/docs/Cropped%20demo.gif)


## References

- [Google API Docs](https://ai.google.dev/gemini-api/docs/document-processing?lang=python)