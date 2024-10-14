from fastapi import FastAPI
import uvicorn
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import json
from system_prompt import get_system_prompt
from utils.getData import getExtractedData
import random


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def sanitize_json(response_string):
    response_string = response_string.replace("```", "").replace("json", "").strip()
    parsed_data = json.loads(response_string)
    return parsed_data


@app.post("/api/v1/analyze")
async def analyze_risk(data: dict):

    llm = ChatOpenAI(api_key=api_key, model="gpt-4o")

    system_prompt = json.dumps(get_system_prompt())

    knowledge = getExtractedData()

    content = system_prompt + knowledge

    user_data = """
    Below is the data provided by the user for analysis:
    """ + json.dumps(
        data, indent=4
    )

    messages = [
        {"role": "system", "content": content},
        {"role": "user", "content": user_data},
    ]

    response = llm.invoke(messages)
    response = sanitize_json(response.content)

    return {"success": True, "data": response}
