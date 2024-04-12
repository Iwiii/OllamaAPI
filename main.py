from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import ollama

class Message(BaseModel):
    role: str
    content: str

app = FastAPI()
client = ollama.Client()

@app.post("/chat")
async def chat(model: str, messages: List[Message]):
    messages_dict = [message.dict() for message in messages]
    response = client.chat(model=model, messages=messages_dict)
    return response

@app.post("/embeddings")
async def embeddings(model: str, messages: List[str]):
    response = client.embeddings(model=model, messages=messages)
    return response

@app.get("/pull/{model}")
async def pull(model: str):
  
    response = client.pull(model=model)
    return response

@app.get("/list")
async def list_models():
    response = client.list()
    return response

@app.get("/show/{model}")
async def show(model: str):
    response = client.show(model=model)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8008,reload=True)