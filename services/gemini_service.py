from google import genai


class GeminiService:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)

    def gerar_resposta(self, medicamento: str, pergunta: str) -> str:
        """
        Gera uma resposta usando o modelo Gemini.
        """

        prompt = f"""
        Medicamento: {medicamento}
        Pergunta: {pergunta}
        Responda de forma clara e objetiva para um paciente.
        """

        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return response.text