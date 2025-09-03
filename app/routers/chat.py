from fastapi import APIRouter, Request

from app.services.chatbot.chat import ChatbotChat
from app.services.chatbot import ChatbotRequest, ChatbotResponse


router = APIRouter(
    prefix="/chat-answer",
    tags=["chatbot"],
    responses={404: {"description": "Not found"}},
)


@router.post("/chat")
def chat(request: Request):
    params = ChatbotRequest(**request.body)
    response: ChatbotResponse = ChatbotChat(params).reply()
    return response.__dict__
