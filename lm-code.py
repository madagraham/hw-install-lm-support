import os
from dotenv import find_dotenv, load_dotenv

# locate and laod environment variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# OpenAI API key and path to installation documents
API_KEY = os.getenv("API_KEY")
PATH_TO_DOCS = os.getenv("PATH_TO_DOCS")
