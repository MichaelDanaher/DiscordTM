import discord
from discord.ext import commands
import tracemalloc
import os
# idk why i need tracemalloc but it doesnt work without it :shrug: 

tracemalloc.start()



with open("username.txt", "r") as userFile:
    username = userFile.read()
with open("secrettoken.txt", "r") as tokenFile:
    token = tokenFile.read()
with open("discordChannel.txt", "r") as channelFile:
    channelNumber = channelFile.read()
# gets username + token + channel id from files


bot = commands.Bot(intents=discord.Intents.default(), command_prefix="!")
# idk why i need a command prefix but it doesnt work without it 

print("Type \"!!!\" to exit. ")


# sends message (no idea why it needs async)
@bot.event
async def on_ready():
    while True:
        message = input(": ")
        if message == "!!!":
            print("Exiting...")
            break

        # sends stuff
        payload = (f"{username}: {message}")
        channel = bot.get_channel(int(channelNumber))
        await channel.send(payload)

# run bot
bot.run(token)