import discord
from discord.ext import commands
import tracemalloc
import os
# doesnt work without traceomalloc

tracemalloc.start()



with open("username.txt", "r") as userFile:
    username = userFile.read()
with open("secrettoken.txt", "r") as tokenFile:
    token = tokenFile.read()
with open("discordChannel.txt", "r") as channelFile:
    channelNumber = channelFile.read()
# gets username + token + channel id from files


bot = commands.Bot(intents=discord.Intents.default(), command_prefix="!")

print("Type \"!exit\" to exit. ")


# sends message
@bot.event
async def on_ready():
    while True:
        message = input(f"{username}: ")
        if message == "!exit":
            print("Exiting...")
            os._exit(0)

        # sends stuff
        payload = (f"{username}: {message}")
        channel = bot.get_channel(int(channelNumber))
        await channel.send(payload)

# run bot
bot.run(token)
