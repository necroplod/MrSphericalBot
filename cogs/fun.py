import discord
import random
from discord.ext import commands

from assets.images import Fun
from assets.images import Stickers


class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def catkdk(self, ctx):
        embed = discord.Embed()
        embed.color = discord.Color.random()
        url = random.choice(Fun.catkdk)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command()
    async def kdk(self, ctx):
        embed = discord.Embed()
        embed.color = discord.Color.random()
        url = random.choice(Fun.kdk)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command()
    async def kdkeat(self, ctx):
        embed = discord.Embed()
        embed.color = discord.Color.random()
        url = Fun.kdkeat
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command()
    async def кринж(self, ctx):
        embed = discord.Embed()
        embed.color = discord.Color.random()
        url = Stickers.кринж
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command()
    async def лох(self, ctx):
        embed = discord.Embed()
        embed.color = discord.Color.random()
        url = Stickers.лох
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command()
    async def украина(self, ctx):
        embed = discord.Embed()
        embed.color = discord.Color.random()
        url = Stickers.украина
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command()
    async def да(self, ctx):
        embed = discord.Embed()
        embed.color = discord.Color.random()
        url = Stickers.да
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command()
    async def эй(self, ctx):
        embed = discord.Embed()
        embed.color = discord.Color.random()
        url = Stickers.эй
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command()
    async def бомба(self, ctx):
        embed = discord.Embed()
        embed.color = discord.Color.random()
        url = Stickers.бомба
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command()
    async def осуждаю(self, ctx):
        embed = discord.Embed()
        embed.color = discord.Color.random()
        url = Stickers.осуждаю
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command()
    async def быдло(self, ctx):
        embed = discord.Embed()
        embed.color = discord.Color.random()
        url = Stickers.быдло
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command()
    async def стоп(self, ctx):
        embed = discord.Embed()
        embed.color = discord.Color.random()
        url = Stickers.стоп
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command()
    async def господин(self, ctx):
        embed = discord.Embed()
        embed.color = discord.Color.random()
        url = Stickers.господин
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(fun(client))