import uvicorn
import Sendpush as sp

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
   token: str
   time: int
   
@app.post("/send")
async def create_token(item: Item):
    print("Token created")
    #print(item.token)
    sp.send_data(item.token, item.time)
    return {"token":  item}

@app.get("/")
async def root():
   print("API is connected")
   return {"message": "API is connected"}



if __name__ == "__main__":
    uvicorn.run("main:app",port=8000, reload=True)
#ngrok config add-authtoken 2r8bFq6GpUfmyrs3PIu13bCYU8e_2oQHWK2hWMYP22TazUnax
#ngrok http http://127.0.0.1:8000/
#https://technodevwebsite.blogspot.com/p/https77da-105-155-176-99ngrok-freeapp.html