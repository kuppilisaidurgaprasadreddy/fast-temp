from pydantic import BaseModel #Check types automatically Convert compatible data Raise errors for invalid input

class Message(BaseModel):
    chat_id: str
    sender: str
    message: str


