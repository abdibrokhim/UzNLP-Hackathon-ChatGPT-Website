from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
import openai

from texttospeech import TextToSpeech
from translate import Translator
from copilot import Copilot
from texttoimage import TextToImage


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/api/v1/translate/')
async def translate(text: str):
    translator = Translator()
    a = translator.translate(text)
    return a


@app.post('/api/v1/copilot/')
async def copilot(text: str):
    copilot = Copilot()
    a = copilot.get_answer(text)
    return a


@app.post('/api/v1/tts/')
async def tts(text: str):
    tts = TextToSpeech()
    a = tts.to_speech(text)
    return a


@app.post('/api/v1/tti/')
async def tti(text: str):
    tti = TextToImage()
    a = tti.to_image(text)
    return a
    

if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)
