# aegis-chatbot
Chatbot inteligente desenvolvido em Python com LangChain e Groq API.
🛡️ Aegis Chatbot
Chatbot inteligente com Python e Inteligência Artificial Generativa

O Aegis Chatbot é um projeto acadêmico desenvolvido em grupo durante a graduação em Engenharia de Software. Seu objetivo é criar um assistente virtual capaz de responder perguntas utilizando informações extraídas de uma fonte específica da internet.

🎯 Objetivo do projeto

Desenvolver um chatbot que utiliza Inteligência Artificial para interpretar perguntas e gerar respostas contextualizadas com base no conteúdo disponibilizado, reduzindo respostas que não possuem fundamento na fonte consultada.

⚙️ Tecnologias utilizadas
Python
LangChain
Groq API
Llama 3.3 70B Versatile
WebBaseLoader
Web Scraping
Engenharia de Prompts
🧠 Funcionamento

O Aegis Chatbot realiza as seguintes etapas:

Acessa uma página da internet.
Extrai o conteúdo textual da página.
Organiza as informações para processamento.
Envia o conteúdo e a pergunta do usuário ao modelo de IA.
Apresenta uma resposta baseada no material fornecido.
Informa quando não encontra a informação solicitada.
📂 Estrutura do projeto
text
aegis-chatbot/
│
├── chatbot.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE

🚀 Como executar
1. Clonar o projeto
bash
git clone https://github.com/SEU-USUARIO/aegis-chatbot.git

2. Entrar na pasta
bash
cd aegis-chatbot

3. Instalar as dependências
bash
pip install -r requirements.txt

4. Configurar a chave da Groq

Configure a variável de ambiente GROQ_API_KEY com sua chave pessoal.

No Windows PowerShell:

powershell
$env:GROQ_API_KEY="SUA_CHAVE"


Não compartilhe sua chave de API.

5. Executar o chatbot
bash
python chatbot.py

💬 Exemplo de utilização
text
Digite sua pergunta: O que é inteligência artificial?

Resposta do Aegis Chatbot:
[Resposta baseada no conteúdo consultado.]

Digite sua pergunta: x

Encerrando o Aegis Chatbot...

📚 Conhecimentos desenvolvidos
Programação em Python.
Integração com APIs.
Inteligência Artificial Generativa.
Processamento de informações.
Engenharia de Prompts.
Desenvolvimento de aplicações interativas.
👥 Equipe

Projeto acadêmico desenvolvido em grupo.

Curso: Engenharia de Software

Integrantes:

[Nome do integrante 1]
[Nome do integrante 2]
[Seu nome]
📄 Licença

Este projeto utiliza a licença MIT, mediante autorização dos integrantes da equipe.

Projeto acadêmico — Engenharia de Software.
