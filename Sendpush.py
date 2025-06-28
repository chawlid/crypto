import time
import FCMmanager as fcm
from pycoingecko import CoinGeckoAPI
import psycopg2



cg = CoinGeckoAPI()

def get_tokens(token):
    conn = psycopg2.connect(database="defaultdb",
                        host="pg-b7b4af8-notification-a9fb.b.aivencloud.com",
                        user="avnadmin",
                        password="AVNS_lCnbZGqy7vDH06IT2hO",
                        port="28691")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.cryptos WHERE token = %s", (token,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row

def send_data(token, usertime):
 print("Received token:", token)
 print("Received time:", usertime)
 i=0
 while True:
   
   time.sleep(15)
   row =  get_tokens(token) 
   
   if not row[2]:
      print("Stop notification")
      break
   
   i += 0.25
   print("----------------(",i,")-----------------------")
   
   if i == usertime:
      print("Time to send notification")
      i = 0
      data=cg.get_price(ids=row[1], vs_currencies ="usd", include_24hr_change=True)

      coins=row[1].split(",")
      coins.pop(0)
      for coin in coins:
        name=coin
        price = data.get(coin).get("usd")
        percentage= data.get(coin).get("usd_24h_change")
        coin_info = cg.get_coin_by_id(coin)
        symbol = coin_info.get("symbol", "").upper()
        url = f"https://www.coingecko.com/en/coins/{coin}"
        print("CoinGecko URL:",url)
        percentage=round(percentage, 2)
        print("Coin: ", coin)
        print(price)
        print(percentage)

        fcm.sendPush(name,symbol,price,percentage,url,token)
        time.sleep(2)
  

    
   

