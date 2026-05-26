from fastapi import FastAPI # coer too to define the apiroutes,requests,handil and return response
from database import db #object we created in mongodb so no need of connection every time
from models import Message # tye of data that u can acept it 


app = FastAPI() # create an fast api application interface

@app.get("/")
async def home(): # async mean wont block any other request while waiting for mongo db
       return {"status": "Chatbot API is running"} # simple check that api is alive or not  


@app.post("/send-message")# Send message
async def send_message(data: Message):
    message = {
        "chat_id": data.chat_id,
        "sender": data.sender,
        "message": data.message
    }

    await db.messages.insert_one(message)

    return {"status": "message sent"}

# Get messages
@app.get("/messages/{chat_id}")
async def get_messages(chat_id: str):

    messages = []

    cursor = db.messages.find({"chat_id": chat_id})

    async for message in cursor:

        message["_id"] = str(message["_id"])

        messages.append(message) #each message into a list

    return messages