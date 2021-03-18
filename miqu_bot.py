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
    for guild in client.guilds:
        if guild.name == target_guild:
            break
        else:
            sys.exit("Target guild is not found")
    
    print(f'{client.user} is connected to {guild.name}')
    

client.run(token)