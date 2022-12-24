from fastapi import FastAPI
import uvicorn
import json
# from fastapi_cors import CORS, FastAPI_CORS
from gpt import to_gpt

import openai


app = FastAPI()

@app.post('/api')
async def genre_words(question:str):
    """ Check sentense and make report list """

    result = to_gpt(question)
 
    return result

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
