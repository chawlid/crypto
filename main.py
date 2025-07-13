import uvicorn
import Sendpush as sp
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

from fastapi.concurrency import run_in_threadpool

app = FastAPI()

origins = [
   "http://localhost:64218",  # Exemple d'origine autorisée (votre frontend)
   "https://sql-app-sigma.vercel.app",   # Exemple d'un autre domaine
                      # Attention, '*' autorise toutes les origines, à n'utiliser qu'en développement
   ]

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,       # Liste des origines autorisées
   allow_credentials=True,      # Autorise les cookies et en-têtes d'authentification
   allow_methods=["*"],         # Autorise toutes les méthodes HTTP
   allow_headers=["*"],         # Autorise tous les en-têtes
   )

class Item(BaseModel):
   token: str
   time: int 


@app.post("/send")
async def create_token(item: Item):
    
    userToken = item.token
    usertime = item.time 
    await run_in_threadpool(sp.send_data, userToken, usertime)
    return {"token":  item}

@app.get("/")
async def root():
   print("API is connected")
   return {"message": "API is "}

""""
@app.get("/token/")
async def send_token( token: str):
   
   await run_in_threadpool(sp.send_data, token)
   return {"message": "token received"}
"""


#if __name__ == "__main__":
#    uvicorn.run("main:app",host="0.0.0.0",port=8000, reload=True)
#ngrok config add-authtoken 2r8bFq6GpUfmyrs3PIu13bCYU8e_2oQHWK2hWMYP22TazUnax
#ngrok http http://127.0.0.1:8000/
#ngrok http http://0.0.0.0:8000/
#https://technodevwebsite.blogspot.com/p/https77da-105-155-176-99ngrok-freeapp.html
# host="192.168.1.48"
