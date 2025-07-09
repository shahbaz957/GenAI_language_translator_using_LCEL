from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
print("GROQ API Key loaded:", groq_api_key is not None)

model = ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key)
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "Translate the provided text into {language} language"),
    ("user", "{text}")
])

chain = prompt | model | parser

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="LangServe + FastAPI with Groq"
)

add_routes(app, chain, path="/chain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
