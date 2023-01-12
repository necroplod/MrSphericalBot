import discord
from discord.ext import commands

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['CATKDK', 'cATKDK'])
    async def catkdk(self, ctx):
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/994918229233385483/997204446939455598/20210110_164119.jpg")
        await ctx.send(embed=embed)





def setup(client):
    client.add_cog(fun(client))