import emoji

from app.enums import GeminiModel
from app.services.chatbot import ChatbotRequest
from app.tasks.generate import GeminiChatExecutor


class BaseGenerator:
    def __init__(self, params: ChatbotRequest):
        self.params = params

    def _remove_bot_prefix(self, response: str):
        """응답에서 'botName:' 형식의 접두사 제거"""
        answer = response.split(":")
        if len(answer) > 1:
            return ":".join(answer[1:]).strip()
        return answer[0].strip()

    def _clean_text(self, text: str):
        """텍스트에서 이모지 제거"""
        return emoji.replace_emoji(text, replace="")

    @staticmethod
    def _format_chat_messages(messages: list, userName: str, botName: str):
        input_messages = []
        for message in messages:
            if message["role"] == "user":
                input_messages.append(
                    {"role": "user", "content": f"{userName}: {message['content']}"}
                )
            elif message["role"] == "assistant":
                input_messages.append(
                    {"role": "assistant", "content": f"{botName}: {message['content']}"}
                )
        return input_messages


class FlashChatGenerator(BaseGenerator):
    def run(self, model: GeminiModel, persona_prompt: str):
        params = self.params.model_copy()

        input_messages = self._format_chat_messages(
            messages=params.messages,
            userName=params.userName,
            botName=params.botName,
        )

        response, numTokens = GeminiChatExecutor().execute(
            model=model,
            system_prompt=persona_prompt,
            messages=input_messages,
            max_output_tokens=128,
            temperature=1.2,
        )

        answer = self._remove_bot_prefix(response)
        answer = self._clean_text(answer)
        return answer, numTokens
