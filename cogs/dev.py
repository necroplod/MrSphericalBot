import discord
import dislash

from dislash import ActionRow, Button, ButtonStyle
from discord.ext import commands

class dev(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx, extensions):
        self.client.load_extension(f'cogs.{extensions}')
        embed = discord.Embed(
            title = "",
            description = f"Ког **{extensions}** был успешно загружен!",
            color = 0x93ff15
        )
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, extensions):
        self.client.unload_extension(f'cogs.{extensions}')
        embed = discord.Embed(
            title = "",
            description = f"Ког **{extensions}** был успешно отгружен!",
            color = 0xf64c6e
        )
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, extensions):
        self.client.unload_extension(f'cogs.{extensions}')
        self.client.load_extension(f'cogs.{extensions}')
        embed = discord.Embed(
            title = "",
            description = f"Ког **{extensions}** был успешно перезагружен!",
            color = 0xf64c6e
            
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(dev(client))