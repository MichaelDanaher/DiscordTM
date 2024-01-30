import discord
from discord.ext import commands
import os
# required packages

with open("secrettoken.txt", "r") as file:
    fileContents = file.read()
# file containing discord token

# guts of message viewer
def listen():
    inten = discord.Intents.all()

    bot = commands.Bot(intents=inten, command_prefix='🗿')

    # actually sends message
    @bot.event
    async def on_message(message):
        print(f"{message.content}")

    bot.run(fileContents)

listen()