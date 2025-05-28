import uvicorn
import Sendpush as sp

from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.concurrency import run_in_threadpool

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class Item(BaseModel):
   token: str


"""@app.post("/send")
async def create_token(item: Item):
    
    print(item.token)
    print("-------------------------------------------------------------------")
    sp.send_data(item.token)
    return {"token":  item}"""

@app.get("/")
async def root():
   print("API is connected")
   return {"message": "API is "}

@app.get("/token/")
async def send_token( token: str):
   
   await run_in_threadpool(sp.send_data, token)
   return {"message": "token received"}



if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000, reload=True)
#ngrok config add-authtoken 2r8bFq6GpUfmyrs3PIu13bCYU8e_2oQHWK2hWMYP22TazUnax
#ngrok http http://127.0.0.1:8000/
#ngrok http http://0.0.0.0:8000/
#https://technodevwebsite.blogspot.com/p/https77da-105-155-176-99ngrok-freeapp.html
# host="192.168.1.48"