# -*- coding: utf-8 -*-
"""final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uxHOjsn1qDyXkUNyE6htf3NXCfNcV837
"""

!python --version

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install "openai>=1" "langchain>=0.0.331rc2" "unstructured[all-docs]" pillow pydantic lxml pillow matplotlib chromadb tiktoken watermark

!pip install --upgrade --quiet  langchain-google-genai pillow langchain_anthropic

!pip install tensorflow-probability imageio pillow

!pip install open_clip_torch torch

!pip install -U langchain openai chromadb langchain-experimental

image_dir='./Data'

import os
print(os.getcwd())

pdfs=['./yamaha_file1.pdf','./yamaha_file2.pdf','./yamaha_file3.pdf']

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_anthropic import ChatAnthropic
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

import openai
import os

# find API key in console at https://platform.openai.com/account/api-keys

os.environ["OPENAI_API_KEY"] = 'Your Api Key here'
# openai.api_key='Your Api Key here'
openai.api_key = os.environ["OPENAI_API_KEY"]

# langsmith traces

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"]="ls__462be98ad9d44f0b897cd9381e5de36c"
os.environ["LANGCHAIN_PROJECT"]="default"
import getpass
import os

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyD7ROb6ZcuE3DHj0_VBtXDA4WA6Lqx2a8s"

from IPython.display import display, HTML

def plt_img_base64(img_base64):

    # Create an HTML img tag with the base64 string as the source
    image_html = f'<img src="data:image/jpeg;base64,{img_base64}" />'

    # Display the image by rendering the HTML
    display(HTML(image_html))

# plt_img_base64(img_base64_list[1])

import json
with open('./Data_json/table_dict_final.json', 'rb') as file:
    table_dict = json.load(file)
with open('./Data_json/table_summaries.json', 'rb') as file:
    table_summaries = json.load(file)
with open('./Data_json/text_dict_final.json', 'rb') as file:
    text_dict = json.load(file)
# with open('./Data_json/elem_text_dict_yamaha_file1.json', 'rb') as file:
#     elem_dict_yamaha_file1 = json.load(file)
# with open('./Data_json/elem_text_dict_yamaha_file2.json', 'rb') as file:
#     elem_dict_yamaha_file2 = json.load(file)
# with open('./Data_json/elem_text_dict_yamaha_file3.json', 'rb') as file:
#     elem_dict_yamaha_file3 = json.load(file)
with open('./Data_json/base64_to_path.json', 'rb') as file:
    base64_to_path = json.load(file)
with open('./Data_json/base64_to_additional_context.json', 'rb') as file:
    base64_to_additional_context = json.load(file)
with open('./Data_json/image_base64.json', 'rb') as file:
    image_base64 = json.load(file)
with open('./Data_json/image_summary_all.json', 'rb') as file:
    image_summary_all = json.load(file)
# with open('/content/text_dict.json', 'rb') as file:
#     text_dict = json.load(file)

from langchain_google_genai import GoogleGenerativeAIEmbeddings

import uuid
from langchain.vectorstores import Chroma
from langchain.storage import InMemoryStore
from langchain.schema.document import Document
# from langchain.embeddings import OpenAIEmbeddings
# from langchain_openai import OpenAIEmbeddings
from langchain.retrievers.multi_vector import MultiVectorRetriever

# The vectorstore to use to index the child chunks
vectorstore_doc2 = Chroma(collection_name="multi_modal_rag_2",
                     embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001")) #OpenAIEmbeddings()


# The storage layer for the parent documents
store_doc2 = InMemoryStore()
id_key_doc2 = "doc_id_doc2"

# The retriever (empty to start)
retriever_doc2 = MultiVectorRetriever(
    vectorstore=vectorstore_doc2,
    docstore=store_doc2,
    id_key=id_key_doc2
)

vectorstore_doc1 = Chroma(collection_name="multi_modal_rag_1",
                     embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001")) #OpenAIEmbeddings()


# The storage layer for the parent documents
store_doc1 = InMemoryStore()
id_key_doc1 = "doc_id_doc1"

# The retriever (empty to start)
retriever_doc1 = MultiVectorRetriever(
    vectorstore=vectorstore_doc1,
    docstore=store_doc1,
    id_key=id_key_doc1
)
vectorstore_doc3 = Chroma(collection_name="multi_modal_rag_3",
                     embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001")) #OpenAIEmbeddings()


# The storage layer for the parent documents
store_doc3 = InMemoryStore()
id_key_doc3 = "doc_id_doc3"

# The retriever (empty to start)
retriever_doc3 = MultiVectorRetriever(
    vectorstore=vectorstore_doc3,
    docstore=store_doc3,
    id_key=id_key_doc3)

import os
import uuid

import chromadb
import numpy as np
from langchain_community.vectorstores import Chroma
from langchain_experimental.open_clip import OpenCLIPEmbeddings
from PIL import Image as _PILImage

db1 = Chroma(collection_name="yamaha_file1", persist_directory="./chroma_db", embedding_function=OpenCLIPEmbeddings())
retriever_1 = db1.as_retriever()

db2 = Chroma(collection_name="yamaha_file2", persist_directory="./chroma_db", embedding_function=OpenCLIPEmbeddings())
retriever_2 = db2.as_retriever()

db3 = Chroma(collection_name="yamaha_file3", persist_directory="./chroma_db", embedding_function=OpenCLIPEmbeddings())
retriever_3 = db3.as_retriever()

model = ChatAnthropic(temperature=0, api_key="", model_name="claude-3-opus-20240229")

import base64
import io
from io import BytesIO

import numpy as np
from PIL import Image


def resize_base64_image(base64_string, size=(128, 128)):
    """
    Resize an image encoded as a Base64 string.

    Args:
    base64_string (str): Base64 string of the original image.
    size (tuple): Desired size of the image as (width, height).

    Returns:
    str: Base64 string of the resized image.
    """
    # Decode the Base64 string
    img_data = base64.b64decode(base64_string)
    img = Image.open(io.BytesIO(img_data))

    # Resize the image
    resized_img = img.resize(size, Image.LANCZOS)

    # Save the resized image to a bytes buffer
    buffered = io.BytesIO()
    resized_img.save(buffered, format=img.format)

    # Encode the resized image to Base64
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def is_base64(s):
    """Check if a string is Base64 encoded"""
    try:
        return base64.b64encode(base64.b64decode(s)) == s.encode()
    except Exception:
        return False


def split_image_text_types_image(docs):
    """Split numpy array images and texts"""
    images = []
    text = []
    retriever_output=[]
    for doc in docs:
        doc = doc.page_content  # Extract Document contents
        if is_base64(doc):
            # Resize image to avoid OAI server error
            images.append(
                resize_base64_image(doc, size=(250, 250))
            )  # base64 encoded str
        else:
            text.append(doc)
    retriever_output.append({
        "images": images,
        "texts": text
    })
    return {"images": images, "texts": text}

!pip install langchainhub

with open('./Data_json/table_dict_final.json', 'rb') as file:
    table_dict = json.load(file)
with open('./Data_json/table_summaries.json', 'rb') as file:
    table_summaries = json.load(file)
with open('./Data_json/text_dict_final.json', 'rb') as file:
    text_dict = json.load(file)

len(text_dict['yamaha_file1.pdf'])

temp=[]

for i in text_dict['yamaha_file3.pdf']:
    if(i!=''):
        temp.append(i)

len(temp)

text_dict['yamaha_file3.pdf']=temp

from operator import itemgetter
from langchain.schema.runnable import RunnablePassthrough,RunnableLambda
from langchain.schema.messages import HumanMessage,SystemMessage
def prompt_func_new(dict):
    content = [
        {
            "type": "text",
            "text": f"Answer the question based only on the following context, which includes the below image: Question: {dict['question']}"
        }
    ]

    # if dict["context"]["images"]:
    try:
        image_content = [
                {
                    "type": "text",
                    "text": f"must you use the image below, always mention the page number from where the image is from. The page number where the image is from is {base64_to_path[dict['context']['images'][0]].split('-')[1]} You are also provided with the additional context consisting of both the text and tables on the same page as the image provided. You may refer to that to understand the context of the image and may help answering the query \\ Additional context Text: {base64_to_additional_context[dict['context']['images'][0]][1]}  \\n\\n Additional context Tables: {base64_to_additional_context[dict['context']['images'][0]][0]}"
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{dict['context']['images'][0]}"}
                },
                {
                    "type": "text",
                    "text": f"must you use the image below, always mention the page number from where the image is from. The page number where the image is from is {base64_to_path[dict['context']['images'][1]].split('-')[1]} You are also provided with the additional context consisting of both the text and tables on the same page as the image provided. You may refer to that to understand the context of the image and may help answering the query \\ Additional context Text: {base64_to_additional_context[dict['context']['images'][1]][1]}  \\n\\n Additional context Tables: {base64_to_additional_context[dict['context']['images'][1]][0]}"
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{dict['context']['images'][1]}"}
                }
            ]
    except:
        print("*")
        image_content = [
                {
                    "type": "text",
                    "text": f"must you use the image below, always mention the page number from where the image is from."
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{dict['context']['images'][0]}"}
                },
                {
                    "type": "text",
                    "text": f"must you use the image below, always mention the page number from where the image is from."
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{dict['context']['images'][1]}"}
                }
            ]
    content.extend(image_content)

    return [HumanMessage(content=content)]

chain_1 = (
    {
        "context": retriever_1 | RunnableLambda(split_image_text_types_image),
        "question": RunnablePassthrough(),
    }
    | RunnableLambda(prompt_func_new)
    | model
    | StrOutputParser()
)

chain_2 = (
    {
        "context": retriever_2 | RunnableLambda(split_image_text_types_image),
        "question": RunnablePassthrough(),
    }
    | RunnableLambda(prompt_func_new)
    | model
    | StrOutputParser()
)

chain_3 = (
    {
        "context": retriever_3 | RunnableLambda(split_image_text_types_image),
        "question": RunnablePassthrough(),
    }
    | RunnableLambda(prompt_func_new)
    | model
    | StrOutputParser()
)

# Import things that are needed generically
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
# from langchain_openai import OpenAI

from langchain import LLMMathChain

prompt = hub.pull("hwchase17/react")

llm_math=LLMMathChain.from_llm(model, verbose=True)

from langchain.agents import Tool

tools = [
    Tool(
        name='MTN1000D (MT-10 SP) OWNERS MANUAL',
        func=chain_1.invoke,
        description=(
            'Use this tool when answering queries regarding information about MTN1000D (MT-10 SP) model. Input should be a well-formed question.'
        )
    ),
    Tool(
        name='YZF1000 (YZF-R1) and YZF1000D (YZF-R1M) OWNERS MANUAL',
        func=chain_2.invoke,
        description=(
            'Use this tool when answering queries regarding information about YZF1000 (YZF-R1) and YZF1000D (YZF-R1M) models. Input should be a well-formed question.'
        )
    ),
    Tool(
        name='MTN890D (MT-09 SP) OWNERS MANUAL',
        func=chain_3.invoke,
        description=(
            'Use this tool when answering queries regarding information about MTN890D (MT-09 SP) model. Input should be a well-formed question.'
        )
    ),
    Tool(
        name="mathematics operator",
        func=llm_math.run,
        description=('Use this tool when you want to perform any mathematical operation.Input should be a well-formed question.')
    ),
    Tool(
        name="image Database of MTN1000D (MT-10 SP) OWNERS MANUAL",
        func=chain_1.invoke,
        description=('this tool contains the images present in the MTN1000D (MT-10 SP) OWNERS MANUAL.Use this when you have to use images from the pdf MTN1000D (MT-10 SP) OWNERS MANUAL')
    ),
    Tool(
        name="image Database of YZF1000 (YZF-R1) and YZF1000D (YZF-R1M) OWNERS MANUAL",
        func=chain_2.invoke,
        description=('this tool contains the images present in the YZF1000 (YZF-R1) and YZF1000D (YZF-R1M) OWNERS MANUAL.Use this when you have to use images from the pdfYZF1000 (YZF-R1) and YZF1000D (YZF-R1M) OWNERS MANUAL')
    ),
    Tool(
        name="image Database of MTN890D (MT-09 SP) OWNERS MANUAL",
        func=chain_3.invoke,
        description=('this tool contains the images present in the MTN890D (MT-09 SP) OWNERS MANUAL.Use this when you have to use images from the pdf MTN890D (MT-09 SP) OWNERS MANUAL')
    )
]

from langchain.agents import create_react_agent
agent = create_react_agent(model, tools, prompt)
# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, return_intermediate_steps=True,handle_parsing_errors=True)

retriever_output = []

retriever_output

response = agent_executor.invoke({"input": "hii can you summarize the YZF1000 (YZF-R1) and YZF1000D (YZF-R1M) OWNERS MANUAL"})



response

# Add texts
doc_ids = [str(uuid.uuid4()) for _ in text_dict['yamaha_file1.pdf']]
summary_texts = [
    Document(page_content=s, metadata={id_key_doc1: doc_ids[i]})
    for i, s in enumerate(text_dict['yamaha_file1.pdf'])
]
retriever_doc1.vectorstore.add_documents(summary_texts)
retriever_doc1.docstore.mset(list(zip(doc_ids, text_dict['yamaha_file1.pdf'])))

# Add tables
table_ids = [str(uuid.uuid4()) for _ in table_dict['yamaha_file1.pdf']]
summary_tables = [
    Document(page_content=s, metadata={id_key_doc1: table_ids[i]})
    for i, s in enumerate(table_summaries['yamaha_file1.pdf'])
]
retriever_doc1.vectorstore.add_documents(summary_tables)
retriever_doc1.docstore.mset(list(zip(table_ids, table_dict['yamaha_file1.pdf'])))

# Add texts
doc_ids = [str(uuid.uuid4()) for _ in text_dict['yamaha_file2.pdf']]
summary_texts = [
    Document(page_content=s, metadata={id_key_doc2: doc_ids[i]})
    for i, s in enumerate(text_dict['yamaha_file2.pdf'])
]
retriever_doc2.vectorstore.add_documents(summary_texts)
retriever_doc2.docstore.mset(list(zip(doc_ids, text_dict['yamaha_file2.pdf'])))

# Add tables
table_ids = [str(uuid.uuid4()) for _ in table_dict['yamaha_file2.pdf']]
summary_tables = [
    Document(page_content=s, metadata={id_key_doc2: table_ids[i]})
    for i, s in enumerate(table_summaries['yamaha_file2.pdf'])
]
retriever_doc2.vectorstore.add_documents(summary_tables)
retriever_doc2.docstore.mset(list(zip(table_ids, table_dict['yamaha_file2.pdf'])))

# Add texts
doc_ids = [str(uuid.uuid4()) for _ in text_dict['yamaha_file3.pdf']]
summary_texts = [
    Document(page_content=s, metadata={id_key_doc3: doc_ids[i]})
    for i, s in enumerate(text_dict['yamaha_file3.pdf'])
]
retriever_doc3.vectorstore.add_documents(summary_texts)
retriever_doc3.docstore.mset(list(zip(doc_ids, text_dict['yamaha_file3.pdf'])))

# Add tables
table_ids = [str(uuid.uuid4()) for _ in table_dict['yamaha_file3.pdf']]
summary_tables = [
    Document(page_content=s, metadata={id_key_doc3: table_ids[i]})
    for i, s in enumerate(table_summaries['yamaha_file3.pdf'])
]
retriever_doc3.vectorstore.add_documents(summary_tables)
retriever_doc3.docstore.mset(list(zip(table_ids, table_dict['yamaha_file3.pdf'])))

