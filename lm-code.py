import os
import openai
import PyPDF2

from dotenv import find_dotenv, load_dotenv

# locate and laod environment variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# OpenAI API key and path to installation documents
openai.api_key = os.getenv("OPENAI_API_KEY")
path_to_docs = os.getenv("PATH_TO_DOCS")

# Define a function to search through text documents for a user's question
def search_docs(question, docs_dir):
    answers = []
    for filename in os.listdir(docs_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(docs_dir, filename), "r") as f:
                text = f.read()
                response = openai.Completion.create(
                    engine="davinci", 
                    prompt=f"{question}\n\n{text}",
                    max_tokens=1024, 
                    temperature=0.5, 
                    n=1, 
                    stop=None,
                )
                answer = response.choices[0].text.strip()
                answers.append((filename, answer, response.choices[0].score))
    answers = sorted(answers, key=lambda x: x[2], reverse=True)
    return answers

# converts .pdf files to .txt for all files in installation-documents folder
for filename in os.listdir(path_to_docs):
    # check if the file is a .pdf or .txt file
    if filename.endswith(".pdf"):
        # open .pdf file
        with open(os.path.join(path_to_docs, filename), "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            # empty list to store the extracted text
            text_list = []
            # get number of pages and go through all pages in .pdf
            num_pages = len(pdf_reader.pages)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                txt_filename = filename[:-4] + f"_page{page_num+1}.txt"
                # append text to the list
                text_list.append(text)
            # save as .txt
            with open(os.path.join(path_to_docs, os.path.splitext(txt_filename)[0] + ".txt"), "w") as txt_file:
                txt_file.write("\n".join(text_list))
    elif filename.endswith(".txt"):
        # prompt the user to enter a question
        question = input("Enter your question: ")

        # search for the answer to the user's question in the text documents
        answers = search_docs(question, path_to_docs)

        # print the top answer
        if answers:
            print(f"The top answer to your question is: {answers[0][1]}")
        else:
            print("Sorry, I could not find an answer to your question.")
    else:
        continue









