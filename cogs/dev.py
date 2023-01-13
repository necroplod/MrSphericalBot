import datetime
import discord

from discord.ext import commands

class dev(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx, extensions):
        if extensions.startswith('handlers'):
            await self.client.load_extension(f'handlers.{extensions}')
        await self.client.load_extension(f'cogs.{extensions}')
        embed = discord.Embed(
            title = "",
            description = f"Ког **{extensions}** был успешно загружен!",
            color = 0x93ff15
        )
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, extensions):
        if extensions.startswith('handlers'):
            await self.client.unload_extension(f'handlers.{extensions}')
        await self.client.unload_extension(f'cogs.{extensions}')
        embed = discord.Embed(
            title = "",
            description = f"Ког **{extensions}** был успешно отгружен!",
            color = 0xf64c6e
        )
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, extensions):
        if extensions.startswith('handlers'):
            await self.client.unload_extension(f'handlers.{extensions}')
            await self.client.load_extension(f'handlers.{extensions}')
        await self.client.unload_extension(f'cogs.{extensions}')
        await self.client.load_extension(f'cogs.{extensions}')
        embed = discord.Embed(
            title = "",
            description = f"Ког **{extensions}** был успешно перезагружен!",
            color = 0xf64c6e
            
        )
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send(f"```Shutdown {self.client.user.name} : {str(datetime.datetime.now())}```")
        await self.client.close()

async def setup(client):
    await client.add_cog(dev(client))