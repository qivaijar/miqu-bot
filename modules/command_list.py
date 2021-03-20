# import required libraries
import yaml
import asyncio
import discord
from discord.ext import commands
from googlesearch import search 
import yaml
import numpy as np

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def typed(self, ctx, *message):
        """Return typed message"""
        message = " ".join(message)
        await ctx.send(f'You typed: {message}')

    @commands.command()
    async def g(self, ctx, *message):
        """Return user typed message"""
        searchContent = ""
        text = message
        for i in range(0, len(text)):
            searchContent = searchContent + text[i]

        for j in search(searchContent, num=1, stop=1):
            await ctx.send(j)

    @commands.command()
    async def roll(self, ctx, *message):
        """Return typed message"""
        random_number = np.random.randint(low=1,high=100)
        await ctx.send(f'{ctx.author.name}, You rolled: {random_number}')