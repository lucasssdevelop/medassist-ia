from dotenv import load_dotenv
import os
from gemini_service import GeminiService

# Carrega variáveis do arquivo .env
load_dotenv()

def main():
    # Busca a chave de forma segura
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Erro: API key não encontrada. Verifique seu arquivo .env")
        return

    # Inicializa o serviço
    service = GeminiService(api_key)

    # Entrada do usuário
    medicamento = input("Informe o medicamento: ")
    pergunta = input("Digite sua pergunta: ")

    # Prompt estruturado (boa prática)
    prompt = f"""
Você é um assistente de orientação farmacológica.

Medicamento: {medicamento}

Pergunta:
{pergunta}

Responda de forma objetiva e clara.
"""

    try:
        resposta = service.enviar_pergunta(prompt)

        print("\nResposta:")
        print(resposta)

    except Exception as e:
        print("\nErro ao consultar a API:")
        print(str(e))


if __name__ == "__main__":
    main()