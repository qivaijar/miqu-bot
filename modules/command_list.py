# import required libraries
import yaml
import asyncio
import discord
from discord.ext import commands
import yaml

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def typed(self, ctx, *message):
        """Return user typed message"""
        message = " ".join(message)
        await ctx.send(f'You typed: {message}')
