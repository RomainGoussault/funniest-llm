from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from ollama import generate


app = FastAPI()


class Text(BaseModel):
    text: str
    date: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/summarize")
def summarize_text(text: str) -> str:

    llm = "llama3.2:1b"

    prompt : str = "Summarize this text in one sentence: " + text

    response = generate(llm, prompt, stream=False)["response"]

    return response
