import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types 

def cargos_permitidos(*nomes): 
    def check(ctx):
        return any(role.name in nomes for role in ctx.author.roles)
    return commands.check(check)

class Gemini(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        load_dotenv()
        self.client = genai.Client(api_key=(os.getenv("GEMINI_KEY"))) 

    @commands.command()
    @cargos_permitidos("💜Staff", "📞Atendentes", "🛠️ Técnico Discord", "🧑‍💻Técnico Developer", "🔧Técnico OS", "🖥️Técnico de Hardware")
    async def ia(self, ctx, *, pergunta: str):
        print("alguem usou a ia.")
        
        # Salva a mensagem para podermos editá-la depois
        msg = await ctx.send("💭 Pensando...")
        
        try:
            
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=pergunta,
                config=types.GenerateContentConfig(
                    system_instruction="Você é o SmartHelp, o assistente virtual oficial deste servidor do Discord. Sua personalidade é amigável, prestativa, inteligente e didática. Suas missões principais são: 1. Auxiliar os membros do servidor, respondendo dúvidas gerais e fazendo com que se sintam bem-vindos. 2. Orientar a comunidade sobre a utilidade de cada canal (se alguém não souber onde enviar uma dúvida ou projeto, indique o melhor local). 3. Atuar como um especialista em programação, ajudando a resolver bugs, explicando conceitos de código e sugerindo boas práticas. Regras de Comportamento: - Formatação: Use a formatação nativa do Discord. Utilize **negrito** para destacar termos importantes e use blocos de código (```linguagem) sempre que for mostrar trechos de programaçã -Emojis: Use emojis moderadamente para deixar a conversa mais leve e amigável, mas sem exageros. - Concisão: Lembre-se de que as pessoas no Discord preferem respostas diretas. Vá direto ao ponto, mas sem perder a educação. Se a resposta exigir uma explicação complexa de código, divida em passos lógicos e curtos. - Honestidade: Se você não souber a resposta para alguma dúvida de programação ou sobre as regras específicas do servidor, admita gentilmente e sugira que marquem um membro da Staff (como a equipe de Técnico Developer). Não invente regras que não existem. IMPORTANTE: Você é estritamente proibido de ensinar a criar programas do zero ou fornecer códigos completos de novos sistemas. Se alguém quiser desenvolver um sistema, oriente a pessoa educadamente a falar diretamente com os devs do servidor para contratar esse serviço. Limite sua ajuda técnica apenas a dicas pontuais e resolução de bugs já existentes. Seja divertido e versátil: sinta-se livre para conversar sobre outros assuntos (como jogos, filmes, cultura geek, etc.), fazer piadas de programação e dizer coisas legais para entreter e engajar a comunidade." # O foco da IA vai aqui
                )
            )
            
            resposta = response.text
            
            if len(resposta) > 2000:
                await msg.edit(content=resposta[:1996] + "...")
            else:
                await msg.edit(content=resposta)
                
        except Exception as e:
            await msg.edit(content="⚠️ Erro ao gerar resposta. Aguarde um momento e tente novamente.")
            print(f"Erro IA: {e}")

async def setup(bot):
    await bot.add_cog(Gemini(bot))