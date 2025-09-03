from app.services.chatbot import ChatbotRequest


class PromptCreator:
    def __init__(self, params: ChatbotRequest):
        self.params = params

    def get_instruction(self):
        subject = "#명령문"
        contents = [
            f"너는 {self.params.botName}의 정보를 최대한 반영하여 현재 상황에 가장 알맞는 {self.params.botName}의 대답을 작성해야해",
        ]
        output = f"{subject}\n"
        for content in contents:
            output += f"{content}\n"

        return output

    def get_bot_description(self):
        # 봇 특징 추가
        output = ""
        for descriptions in self.params.perDescriptions:
            output += f"#{self.params.botName}의 {descriptions['subject']}\n"
            for line in descriptions["content"].split("\n"):
                if line.strip():  # Only add non-empty lines
                    output += f"{line.strip()}\n"
            output += "\n"

        return output

    def get_thinking_steps(self):
        subject = f"## {self.params.botName}의 응답을 생성하기 위해 다음 과정을 반드시 거치세요 ##"
        contents = [
            "1. 요청을 구성 요소별로 분해하고 핵심 제약사항과 요구사항을 명확히 정의해.",
            f"2. '{self.params.botName}'의 프로필을 상세히 분석하여, 핵심 정체성, 성격, 특징 및 '{self.params.userName}'과의 관계를 명확히 정리해.",
            f"3. '{self.params.botName}'가 실제로 하고 있을 법한 활동을 여러 가지 브레인스토밍하여 자연스럽게 반응할 수 있도록 상황을 구체화해.",
            "4. 분석한 정보를 바탕으로, 캐릭터의 성격과 행동 특징을 최대한 반영한 여러 가지 응답 초안을 작성하고 평가해.",
            "5. 최종적으로 응답을 선정하고 세부적인 행동 묘사까지 추가하여 캐릭터를 더욱 생생하게 묘사해.",
            "6. 완성된 응답이 캐릭터 프로필에 완벽히 부합하는지 최종 점검하고 설명을 덧붙혀.",
        ]
        output = f"\n{subject}\n"
        for content in contents:
            output += f"{content}\n"

        return output
