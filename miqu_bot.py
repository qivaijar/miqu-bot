# import libraries
import discord
from discord.ext import commands
from dotenv import load_dotenv
# from modules import command_container as cc
from modules import command_list as cl
from modules import music_commands as mc
import os
import re
import sys
sys.path.append('/mnt/c/ffmpeg/ffmpeg/bin/')

# load .env file (containing secret info)
load_dotenv()

# get discord token and specific guild name
token = os.getenv('miqu_token')
target_guild = os.getenv('guild_name')

client =  commands.Bot(command_prefix=commands.when_mentioned_or("mq"),
                description='Semijipun First Discord Bot. Typed \'mq\' + one of the command below to interact:')

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == target_guild, client.guilds)
    if guild is not None:
        print(f'{client.user} is connected to {guild.name}')
    else:
        sys.exit("Target guild does not match")

client.add_cog(mc.Music(client))
client.add_cog(cl.General(client))
client.run(token)

