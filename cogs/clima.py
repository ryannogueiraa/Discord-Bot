import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('WEATHER_TOKEN')

class Clima(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clima(self, ctx, *, cidade: str):
        print("Alguém solicitou o clima!")
        try:
            
            url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={TOKEN}&lang=pt_br&units=metric"
            dadosresposta = requests.get(url).json()

            if dadosresposta.get("cod") != 200:
                await ctx.send(f"❌ Cidade '{cidade}' não encontrada.")
                return

            nome = dadosresposta["name"]
            temp = dadosresposta["main"]["temp"]
            desc = dadosresposta["weather"][0]["description"].capitalize()
            umidade = dadosresposta["main"]["humidity"]

            embed = discord.Embed(
                title=f"☁️ Clima da cidade {nome}",
                description=f"{desc}",
                color=0x1abc9c
            )
            embed.add_field(name="🌡️ Temperatura", value=f"{temp}°C", inline=True)
            embed.add_field(name="💧 Umidade", value=f"{umidade}%", inline=True)

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"❌ Erro ao mostrar clima: {e}")

async def setup(bot):
    await bot.add_cog(Clima(bot))
