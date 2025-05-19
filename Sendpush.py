import time
import FCMmanager as fcm
from pycoingecko import CoinGeckoAPI
import psycopg2






conn = psycopg2.connect(database="defaultdb",
                        host="pg-b7b4af8-notification-a9fb.b.aivencloud.com",
                        user="avnadmin",
                        password="AVNS_lCnbZGqy7vDH06IT2hO",
                        port="28691")
cg = CoinGeckoAPI()



def get_tokens(token):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.cryptos WHERE token = %s", (token,))
    row = cursor.fetchone()
    
    return row

def send_data(token, timeLoop):

 while True:
   row= get_tokens(token)
   print(row[2])
   if not row[3]:
      print("Stop notification")
      break
   data=cg.get_price(ids=row[1], vs_currencies ="usd", include_24hr_change=True)
   print(data)
   #name= "Ripple"
   #price = data.get("ripple").get("usd")
   #percentage= data.get("ripple").get("usd_24h_change")
   coins=row[1].split(",")
   for coin in coins:
     
    
     name=coin
     price = data.get(coin).get("usd")
     percentage= data.get(coin).get("usd_24h_change")
     print("Coin: ", coin)
     print(price)
     print(percentage)
     fcm.sendPush(name,price,percentage, token)
  
 # send_notification("Cardano", data.get("cardano").get("usd"), data.get("cardano").get("usd_24h_change"))
    
   time.sleep(60)


