from app.enums import GeminiModel
from app.services.prompt.create import PromptCreator
from app.services.chatbot import ChatbotResponse

from app.tasks.generate import FlashChatGenerator


class ChatbotChat(PromptCreator):

    def create_chat_prompt(self):
        prompt = ""
        prompt += self.get_instruction()  # 명령문
        prompt += self.get_bot_description()  # 봇 설명
        prompt += self.get_thinking_steps()  # 생각 과정
        return prompt

    def reply(self) -> ChatbotResponse:
        prompt = self.create_chat_prompt()

        try:
            answer, numTokens = FlashChatGenerator(self.params).run(
                model=GeminiModel.FLASH_V2, persona_prompt=prompt
            )

        except Exception:
            answer, numTokens = FlashChatGenerator(self.params).run(
                model=GeminiModel.FLASH_V2_5, persona_prompt=prompt
            )

        return ChatbotResponse(
            answer=answer,
            num_tokens=numTokens,
        )
