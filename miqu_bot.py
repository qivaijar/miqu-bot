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

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == target_guild, client.guilds)
    if guild is not None:
        print(f'{client.user} is connected to {guild.name}')
    else:
        sys.exit("Target guild does not match")
    

client.run(token)