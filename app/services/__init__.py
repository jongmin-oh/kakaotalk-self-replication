from pydantic import BaseModel

class ChatbotRequest(BaseModel):
    room: str
    msg: str
    sender: str
    isGroupChat: bool
    replier: str
    imageDB: str

class ChatbotResponse(BaseModel):
    response: str