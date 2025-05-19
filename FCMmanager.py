import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def sendPush(name, price_change, percentage_change, registration_token):
    
    # See documentation on defining a message payload.
    message = messaging.Message(
        notification=messaging.Notification(
            title=f"{name} Price : {price_change} USD",
            body=f"The price has changed by {percentage_change}%",
        ),
        token=registration_token,  # Device registration token
    )
    
    response = messaging.send(message)
    print(f"Successfully sent message: {response}")

    
