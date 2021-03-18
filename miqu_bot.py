# import libraries
import discord
from dotenv import load_dotenv
import os
import sys

# load .env file (containing secret info)
load_dotenv()

# get discord token and specific guild name
token = os.getenv('miqu_token')
target_guild = os.getenv('guild_name')
commands_list = os.getenv('commands_list')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == target_guild, client.guilds)
    if guild is not None:
        print(f'{client.user} is connected to {guild.name}')
    else:
        sys.exit("Target guild does not match")

@client.event
async def on_message(message):
    # To make sure that the bot won't respond to its own messages
    if message.author == client.user:
        return

    typed_message = message.content
    if typed_message.startswith('mq'):
        if typed_message.split(" ")[0] not in commands_list:
            await message.channel.send("Miku, Wakannai yo~")
        else:
            await message.channel.send("Miku miku dayo~")
    

client.run(token)