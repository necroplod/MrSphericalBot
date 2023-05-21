import discord
import requests
import random
from discord.ext import commands
from discord import app_commands
from typing import Union

from assets.images import RP


class rp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @app_commands.command(name = "kiss", description = "Поцелуйте кого-нибудь")
    async def kiss(self, interaction: discord.Interaction, участник: Union[discord.Member]):
        embed = discord.Embed(
            description=f"*{interaction.user.mention} поцеловал(а) {участник.mention}*",
            color = discord.Colour.random()
        )
        embed.set_image(url=requests.get("https://purrbot.site/api/img/sfw/kiss/gif").json()['link'])
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "hug", description = "Обнимите кого-нибудь")
    async def hug(self, interaction: discord.Interaction, участник: Union[discord.Member]):
        embed = discord.Embed(
            description=f"*{interaction.user.mention} обнял(а) {участник.mention}*",
            color = discord.Colour.random()
        )
        embed.set_image(url=requests.get("https://purrbot.site/api/img/sfw/hug/gif").json()['link'])
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "pat", description = "Погладьте кого-нибудь")
    async def pat(self, interaction: discord.Interaction, участник: Union[discord.Member]):
        embed = discord.Embed(
            description=f"*{interaction.user.mention} погладил(а) {участник.mention}*",
            color = discord.Colour.random()
        )
        embed.set_image(url=requests.get("https://purrbot.site/api/img/sfw/pat/gif").json()['link'])
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "slap", description = "Ударьте кого-нибудь")
    async def slap(self, interaction: discord.Interaction, участник: Union[discord.Member]):
        embed = discord.Embed(
            description=f"*{interaction.user.mention} ударил(а) {участник.mention}*",
            color = discord.Colour.random()
        )
        embed.set_image(url=requests.get("https://purrbot.site/api/img/sfw/slap/gif").json()['link'])
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "feed", description = "Накормите кого-нибудь")
    async def feed(self, interaction: discord.Interaction, участник: Union[discord.Member]):
        embed = discord.Embed(
            description=f"*{interaction.user.mention} накормил(а) {участник.mention}*",
            color = discord.Colour.random()
        )
        embed.set_image(url=requests.get("https://purrbot.site/api/img/sfw/feed/gif").json()['link'])
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "cry", description = "Заплачьте")
    async def cry(self, interaction: discord.Interaction):
        embed = discord.Embed(
            description=f"*{interaction.user.mention} заплакал(а)*",
            color = discord.Colour.random()
        )
        embed.set_image(url=requests.get("https://purrbot.site/api/img/sfw/cry/gif").json()['link'])
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "tickle", description = "Пощекотите кого-нибудь")
    async def tickle(self, interaction: discord.Interaction, участник: Union[discord.Member]):
        embed = discord.Embed(
            description=f"*{interaction.user.mention} пощекотал(а) {участник.mention}*",
            color = discord.Colour.random()
        )
        embed.set_image(url=requests.get("https://purrbot.site/api/img/sfw/tickle/gif").json()['link'])
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "bite", description = "Укусите кого-нибудь")
    async def bite(self, interaction: discord.Interaction, участник: Union[discord.Member]):
        embed = discord.Embed(
            description = f"*{interaction.user.mention} укусил(а) {участник.mention}*",
            color = участник.color
        )
        url = random.choice(RP.bite)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "sleep", description = "Засните")
    async def sleep(self, interaction: discord.Interaction):
        embed = discord.Embed(
            description = f"*{interaction.user.mention} заснул(а)*",
            color = interaction.user.color
        )
        url = random.choice(RP.sleep)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "eat", description = "Покушайте")
    async def eat(self, interaction: discord.Interaction):
        embed = discord.Embed(
            description = f"*{interaction.user.mention} кушает*",
            color = interaction.user.color
        )
        url = random.choice(RP.eat)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "angry", description = "Разозлитесь")
    async def angry(self, interaction: discord.Interaction):
        embed = discord.Embed(
            description = f"*{interaction.user.mention} в ярости*",
            color = interaction.user.color
        )
        url = random.choice(RP.angry)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "kill", description = "Убейте кого-нибудь")
    async def kill(self, interaction: discord.Interaction, участник: Union[discord.Member]):
        embed = discord.Embed(
            description = f"*{interaction.user.mention} убил(а) {участник.mention}*",
            color = участник.color
        )
        url = random.choice(RP.kill)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "shy", description = "Смущайтесь")
    async def shy(self, interaction: discord.Interaction):
        embed = discord.Embed(
            description = f"*{interaction.user.mention} смущен(а)*",
            color = interaction.user.color
        )
        url = random.choice(RP.shy)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "shake", description = "Пожмите кому-то руку")
    async def shake(self, interaction: discord.Interaction, участник: Union[discord.Member]):
        embed = discord.Embed(
            description = f"*{interaction.user.mention} пожал(а) руку {участник.mention}*",
            color = участник.color
        )
        url = random.choice(RP.shake)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "lick", description = "Лизните кого-нибудь")
    async def lick(self, interaction: discord.Interaction, участник: Union[discord.Member]):
        embed = discord.Embed(
            description = f"*{interaction.user.mention} лизнул(а) {участник.mention}*",
            color = участник.color
        )
        url = random.choice(RP.lick)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "relax", description = "Покайфуйте")
    async def relax(self, interaction: discord.Interaction):
        embed = discord.Embed(
            description = f"*{interaction.user.mention} кайфует*",
            color = interaction.user.color
        )
        url = random.choice(RP.relax)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "dance", description = "Потанцуйте")
    async def dance(self, interaction: discord.Interaction):
        embed = discord.Embed(
            description = f"*{interaction.user.mention} танцует*",
            color = interaction.user.color
        )
        url = random.choice(RP.flex)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "hi", description = "Поприветствуйтесь")
    async def hi(self, interaction: discord.Interaction):
        embed = discord.Embed(
            description = f"*{interaction.user.mention} поприветствовался(ла)*",
            color = interaction.user.color
        )
        url = random.choice(RP.hi)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "bye", description = "Попрощайтесь")
    async def bye(self, interaction: discord.Interaction):
        embed = discord.Embed(
            description = f"*{interaction.user.mention} попрощался(лась)*",
            color = interaction.user.color
        )
        url = random.choice(RP.bye)
        embed.set_image(url=url)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await interaction.response.send_message(embed=embed)
        
async def setup(client):
    await client.add_cog(rp(client))
