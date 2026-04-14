<h1 align="center">🤖 Discord Bot Multifuncional em Python</h1>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=5865F2&size=22&center=true&vCenter=true&width=900&lines=Bot+de+Discord+com+Sistema+de+Moderação;Integração+OpenWeather+e+OpenAI;Jogos+e+Utilidades;Estruturado+com+Cogs+em+Python" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Discord.py-5865F2?style=for-the-badge&logo=discord&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenWeather-FFB703?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Gemini-10A37F?style=for-the-badge"/>
</p>

---

# 🚀 Sobre o Projeto

Bot de Discord desenvolvido em **Python**, organizado com sistema de **Cogs**, contendo comandos de:

- 🔨 Moderação
- 🌤️ Utilidades
- 🎮 Jogos
- 🤖 Inteligência Artificial
- 🎫 Sistema de Suporte

O projeto demonstra organização modular, integração com APIs externas e gerenciamento de permissões no Discord.

---

# 📂 Estrutura do Projeto

📁 projeto
│── main.py
│── .gitignore
│
└── 📁 cogs
    ├── ban.py
    ├── bemvindomsg.py
    ├── clearmsg.py
    ├── clima.py
    ├── expulsar.py
    ├── hora.py
    ├── gemini.py
    ├── piada.py
    ├── ping.py
    ├── pptgame.py
    └── suporte.py


- `main.py` → Inicializa o bot e carrega os Cogs  
- `cogs/` → Comandos organizados por funcionalidades  

---

### 👋 Sistema de Boas-Vindas

- `bemvindomsg.py` → Sistema automático de mensagem de boas-vindas.
- Envia uma mensagem quando um novo membro entra no servidor.

⚠️ É necessário configurar manualmente o ID ou nome do canal onde a mensagem será enviada.

---

# 🧠 Comandos Disponíveis

## 🔨 Moderação

| Comando | Descrição |
|----------|------------|
| `!ban` | Bane um usuário do servidor |
| `!expulsar` | Expulsa um membro |
| `!clearmsg` | Limpa mensagens do canal |

---

## 🌤️ Utilidades

| Comando | Descrição |
|----------|------------|
| `!clima` | Consulta clima via OpenWeather |
| `!hora` | Mostra o horário atual |
| `!ping` | Responde com `pong` |

---

## 🤖 Inteligência Artificial

| Comando | Descrição |
|----------|------------|
| `!ia` | Faz perguntas para IA usando Gemini |
| `!repetirsay` | O bot repete a mensagem enviada |

---

## 🎮 Jogos & Diversão

| Comando | Descrição |
|----------|------------|
| `!ppt (escolha)` | Jogo Pedra, Papel e Tesoura |
| `!piada` | Envia uma piada aleatória |

---

## 🎫 Sistema de Suporte

| Comando | Descrição |
|----------|------------|
| `!suporte` | Cria sistema de ticket ou direciona para call |

⚠️ **Importante:**  
O comando `!suporte` requer configuração manual dos nomes dos canais dentro do servidor para funcionamento correto.

---

## ⚠️ Configuração de Variáveis de Ambiente

Antes de executar o bot, é **obrigatório** criar um arquivo `.env` na raiz do projeto para armazenar suas chaves privadas.

Nunca coloque seu token diretamente no código.

### 📄 Crie um arquivo chamado:

```
.env
```

### 📝 Dentro dele, adicione:

```
DISCORD_TOKEN=seu_token_do_bot_aqui
GEMINI_TOKEN=sua_chave_openai_aqui
OPENWEATHER_TOKEN=sua_chave_openweather_aqui
```

### 🔒 Importante

- Não compartilhe seu arquivo `.env`
- Adicione `.env` ao `.gitignore`
- Nunca publique seus tokens no GitHub

Essas chaves são privadas e dão controle total ao seu bot.


