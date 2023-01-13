import discord
import random
from discord.ext import commands

catkdk = ['https://cdn.discordapp.com/attachments/997425650904338453/1000048326521135205/unknown.png',
         'https://cdn.discordapp.com/attachments/994918229233385483/997204446939455598/20210110_164119.jpg',
         'https://cdn.discordapp.com/attachments/997425650904338453/1000010619572977834/unknown.png'
         ]

kdk = ['https://cdn.discordapp.com/attachments/997425650904338453/1000700313856122900/IMG_20220724_114516.jpg',
      'https://cdn.discordapp.com/attachments/997425650904338453/1000689790854910043/IMG_20220724_110316.jpg',
      'https://cdn.discordapp.com/attachments/997425650904338453/1000685145868730408/20220303_172955.jpg'
      ]

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def catkdk(self, ctx):
        embed = discord.Embed()
        url = random.choice(catkdk)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command()
    async def kdk(self, ctx):
        embed = discord.Embed()
        url = random.choice(kdk)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command()
    async def kdkeat(self, ctx):
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/997425610207006800/1007220298090807317/c63214c00e4d29c0.gif")
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(fun(client))