import functools

import httpx

from google import genai
from google.genai import types

from app.config import GeminConfig
from app.enums import GeminiModel

from app.tasks import Singleton

from app.utility.utils import remove_incomplete_sentence, remove_after_last_punctuation

safety_settings = [
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=types.HarmBlockThreshold.BLOCK_NONE,
    ),
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=types.HarmBlockThreshold.BLOCK_NONE,
    ),
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=types.HarmBlockThreshold.BLOCK_NONE,
    ),
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=types.HarmBlockThreshold.BLOCK_NONE,
    ),
]


def handle_timeout_async():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except httpx.ReadTimeout:
                raise ConnectionError("Gemini Result Timeout")

        return wrapper

    return decorator


def create_contents(messages: list[dict]):
    contents = []
    for message in messages:
        if message["role"] == "user":
            contents.append(
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text=message["content"])],
                )
            )
        elif message["role"] == "assistant":
            contents.append(
                types.Content(
                    role="model",
                    parts=[types.Part.from_text(text=message["content"])],
                )
            )
    return contents


def validate_response(response: types.GenerateContentResponse):
    answer = response.text
    numTokens = response.usage_metadata.total_token_count

    if answer is None:
        raise ConnectionError("GEMINI Result None")

    if answer == "":
        raise ConnectionError("GEMINI Result Empty String")

    if response.candidates[0].finish_reason.name == "MAX_TOKENS":
        answer = remove_incomplete_sentence(answer)

    if len(answer) > 200:  # 대답의 길이가 200자를 넘는 경우
        answer = remove_after_last_punctuation(answer[:200])

    return answer, numTokens


class GeminiChatExecutor(metaclass=Singleton):
    def __init__(self):
        self.client = genai.Client(
            api_key=GeminConfig.API_KEY, http_options=types.HttpOptions(timeout=4000)
        )

    @handle_timeout_async()
    def execute(
        self,
        model: GeminiModel,
        system_prompt: str,
        messages: list[dict],
        max_output_tokens: int,
        temperature: float,
    ):
        contents = create_contents(messages)

        generate_content_config = types.GenerateContentConfig(
            temperature=temperature,
            top_p=0.95,
            max_output_tokens=max_output_tokens,
            response_mime_type="text/plain",
            system_instruction=[types.Part.from_text(text=system_prompt)],
            safety_settings=safety_settings,
        )

        if model == GeminiModel.FLASH_V2_5:
            generate_content_config.thinking_config = types.ThinkingConfig(
                thinking_budget=0
            )

        response = self.client.models.generate_content(
            model=model.value,
            contents=contents,
            config=generate_content_config,
        )

        answer, numTokens = validate_response(response)
        return answer, numTokens
