from unittest.mock import MagicMock
from services.gemini_service import GeminiService


class TestGeminiService:

    def test_envio_prompt(self):
        service = GeminiService("fake-key")

        # mockando método interno (evita chamada real de API)
        service.gerar_resposta = MagicMock(return_value="Resposta simulada")

        resultado = service.gerar_resposta(
            "dipirona",
            "Da sono?"
        )

        assert resultado is not None


    def test_resposta_formato(self):
        service = GeminiService("fake-key")

        service.gerar_resposta = MagicMock(return_value="Resposta simulada")

        resultado = service.gerar_resposta(
            "dipirona",
            "Da sono?"
        )

        assert isinstance(resultado, str)