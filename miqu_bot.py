# import libraries
import discord
from dotenv import load_dotenv
from modules import command_container as cc
from modules import command_list as cl
import os
import re
import sys

# load .env file (containing secret info)
load_dotenv()

# get discord token and specific guild name
token = os.getenv('miqu_token')
target_guild = os.getenv('guild_name')
command_list = os.getenv('command_list')
command_list = command_list.split(" ") # split the string separated by space to get the list of all commands
trigger_word = os.getenv('trigger_word')

client = discord.Client()
# 
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
    if typed_message.startswith(trigger_word):
        typed_command = typed_message.split(" ")[0]
        input_message = typed_message.split(" ")[1::]
        if len(input_message) > 1:
            input_message = " ".join(input_message)

        if len(re.findall(r"(?=("+'|'.join(command_list)+r"))", typed_command)) == 0:
            await message.channel.send("Miku, Wakannai yo~. type mqhelp to see the full command lists")
        else:
            com_con = cc.command_container(typed_command, input_message)
            com_con = com_con.run()
            await eval(com_con)
            
client.run(token)