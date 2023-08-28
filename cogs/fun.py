import discord
import random
from discord.ext import commands
from discord import app_commands

from assets.images import Fun
from assets.images import Stickers


class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @app_commands.command(name = "kdk", description = "Ням, ням пяченьки)")
    async def kdk(
            self, interaction: discord.Interaction
    ):
        embed = discord.Embed(color=discord.Color.random())
        url = random.choice(Fun.kdk)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "кринж", description = "Шо ты высрал?")
    async def кринж(
            self, interaction: discord.Interaction
    ):
        embed = discord.Embed(color=discord.Color.random())
        url = Stickers.кринж
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "лох", description = "Лох.")
    async def лох(
            self, interaction: discord.Interaction
    ):
        embed = discord.Embed(color=discord.Color.random())
        url = Stickers.лох
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "украина", description = "Хрю-хрю, ой...")
    async def украина(
            self, interaction: discord.Interaction
    ):
        embed = discord.Embed(color=discord.Color.random())
        url = Stickers.украина
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "да", description = "да.")
    async def да(
            self, interaction: discord.Interaction
    ):
        embed = discord.Embed(color=discord.Color.random())
        url = Stickers.да
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "эй", description = "Эй..")
    async def эй(
            self, interaction: discord.Interaction
    ):
        embed = discord.Embed(color=discord.Color.random())
        url = Stickers.эй
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "бомба", description = "бууум")
    async def бомба(
            self, interaction: discord.Interaction
    ):
        embed = discord.Embed(color=discord.Color.random())
        url = Stickers.бомба
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "осуждаю", description = "осуждаю, твич не бань")
    async def осуждаю(
            self, interaction: discord.Interaction
    ):
        embed = discord.Embed(color=discord.Color.random())
        url = Stickers.осуждаю
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "быдло", description = "фу, быдло")
    async def быдло(
            self, interaction: discord.Interaction
    ):
        embed = discord.Embed(color=discord.Color.random())
        url = Stickers.быдло
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "стоп", description = "Stop this shit")
    async def стоп(
            self, interaction: discord.Interaction
    ):
        embed = discord.Embed(color=discord.Color.random())
        url = Stickers.стоп
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "господин", description = "господин?")
    async def господин(
            self, interaction: discord.Interaction
    ):
        embed = discord.Embed(color=discord.Color.random())
        url = Stickers.господин
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

async def setup(client):
    await client.add_cog(fun(client))