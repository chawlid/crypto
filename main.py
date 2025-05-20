import uvicorn
import Sendpush as sp
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


class Item(BaseModel):
   token: str
   time: int
   
@app.post("/token/")
async def create_token(item: Item):
    print("Token created")
    print(item.token)
    print(item.time)
    sp.send_data(item.token, item.time)
    return {"token":  item}

@app.get("/")
async def root():
   print("API is connected")
   return {"message": "API is connected"}

@app.get("/send/")
async def send():
    print("Send push notification")
    
    return {"message": "Push notification sent"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)