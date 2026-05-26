from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv #with out this we cant read the url
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL") #fetching fromthe enveronment

client = AsyncIOMotorClient(MONGO_URL) #create a full connection to your atlas cluster (connects the object it mean)


db = client.chatbot_db # cellect the chat bot name in the mandgo db