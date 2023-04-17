import os
import openai
import PyPDF2

from langchain.document_loaders import TextLoader
from dotenv import find_dotenv, load_dotenv

# locate and laod environment variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# OpenAI API key and path to installation documents
openai.api_key = os.getenv("OPENAI_API_KEY")
path_to_docs = os.getenv("PATH_TO_DOCS")

# load document
loader = TextLoader(path_to_docs)