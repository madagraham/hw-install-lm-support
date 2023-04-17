import os
import openai
import PyPDF2

from langchain.document_loaders import TextLoader
from dotenv import find_dotenv, load_dotenv
from langchain.indexes import VectorstoreIndexCreator

# locate and laod environment variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# OpenAI API key and path to installation documents
openai.api_key = os.getenv("OPENAI_API_KEY")
path_to_file = os.getenv("PATH_TO_FILE")

# load document
loader = TextLoader(path_to_file)

# creating index
index = VectorstoreIndexCreator().from_loaders([loader])

# user question
query = input("What is your installation question: ")
index.query_with_sources(query)

print(f"The answer to your question is: {index.query_with_sources(query)}")