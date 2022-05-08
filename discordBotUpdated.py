import discord
import os
from dotenv import load_dotenv

import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.Client()

my_bot = ChatBot(name='PyBot',read_only=True,logic_adapters=['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'])

from chatterbot.trainers import ChatterBotCorpusTrainer

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

@bot.event
async def on_ready():
	guild_count = 0
	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	if message.author.bot: return
	if len(message.content) > 0:
		await message.channel.send(my_bot.get_response(message.content))
	

bot.run(DISCORD_TOKEN)