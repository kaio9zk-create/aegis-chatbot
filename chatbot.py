
import os

from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# =====================================
# AEGIS CHATBOT - PROJETO ACADÊMICO
# =====================================

# Configuração da API
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "Configure a variável de ambiente GROQ_API_KEY antes de executar."
    )

os.environ["USER_AGENT"] = "AegisChatbot/1.0"

# Modelo de inteligência artificial
chat = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=api_key
)

# Carregamento do conteúdo do site
print("Carregando informações...")

loader = WebBaseLoader(
    "https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial"
)

documentos = loader.load()

# Preparação do texto
documento = " ".join(
    [doc.page_content for doc in documentos]
)

documento = documento[:8000]

# Configuração do prompt
template = ChatPromptTemplate.from_messages([
    (
        "system",
        """Você é o Aegis Chatbot, um assistente virtual inteligente.
        Responda utilizando somente o conteúdo fornecido.
        Não invente informações.
        Se a resposta não estiver no material, diga:
        'Não encontrei essa informação no material fornecido.'"""
    ),
    (
        "user",
        "Conteúdo: {documentos_informados}\n\n"
        "Pergunta: {pergunta_do_usuario}"
    )
])

# Criação da cadeia de processamento
chain = template | chat

# Interação com o usuário
print("\n================================")
print("       AEGIS CHATBOT")
print("================================")
print("Faça suas perguntas sobre o conteúdo.")
print("Digite 'x' para encerrar.\n")

while True:

    pergunta = input("Digite sua pergunta: ")

    if pergunta.lower() == "x":
        print("Encerrando o Aegis Chatbot...")
        break

    if not pergunta.strip():
        print("Digite uma pergunta válida.")
        continue

    try:
        resposta = chain.invoke({
            "documentos_informados": documento,
            "pergunta_do_usuario": pergunta
        })

        print("\nResposta do Aegis Chatbot:")
        print(resposta.content)
        print()

    except Exception as erro:
        print(f"Erro ao processar a pergunta: {erro}")
