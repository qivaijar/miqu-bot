# import required libraries
import yaml
import asyncio
import discord
from discord.ext import commands
from googlesearch import search 
import yaml
import os

from google_images_search import GoogleImagesSearch

gis = GoogleImagesSearch('AIzaSyC_s6Ym8-bQAExZriuFAJyOehjG9zms1t8', '142afe207877eed34')

# define search params:
_search_params = {
    'q': '',
    'num': 1,
    'fileType': 'jpg'
}


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
        """Return google search result"""
        searchContent = ""
        text = message
        for i in range(0, len(text)):
            searchContent = searchContent + text[i]

        for j in search(searchContent, num=1, stop=1):
            await ctx.send(j)

    @commands.command()
    async def gim(self, ctx, *message):
        """Return google search result"""
        os.remove('tmp/image.jpg')
        message = " ".join(message)
        _search_params['q'] = message
        gis.search(search_params = _search_params, custom_image_name='image')
        for image in gis.results():
            image.download('tmp')
        with open('tmp/image.jpg', 'rb') as fp: 
            discordImage = discord.File(fp)
            await ctx.send(file = discordImage)