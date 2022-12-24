from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
# from fastapi_cors import CORS, FastAPI_CORS
from gpt import to_gpt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/api')
async def genre_words(question: str):
    """ Check sentense and make report list """

    result = to_gpt(question)
 
    return str(result)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
