from enum import Enum


class GeminiModel(Enum):
    FLASH_V1 = "gemini-1.5-flash-002"
    FLASH_V2_LITE = "gemini-2.0-flash-lite-001"
    FLASH_V2_5_LITE = "gemini-2.5-flash-lite-preview-06-17"
    FLASH_V2 = "gemini-2.0-flash"
    FLASH_V2_5 = "gemini-2.5-flash"
    FLASH_8B = "gemini-1.5-flash-8b"
    PRO_V2_5 = "gemini-2.5-pro"
