import settings

import discord
from discord.ext import commands

class welcome(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome = self.client.get_channel(settings.channels.welcome)
        rules = f"<#959770387204415498>"
        embed = discord.Embed(
            title='',
            description=f'''{member.mention}, Добро Пожаловать на сервер **Мистер Сферический**!       
            Не забудь прочитать {rules}!''',
            color=0x2ecc71
        )

        embed.set_image(url="https://i.ytimg.com/vi/nVzqh0fTARU/hqdefault.jpg")
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await welcome.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        welcome = self.client.get_channel(settings.channels.welcome)
        embed = discord.Embed(
            title='',
            description=f'**{member}** Покинул наш сервер :(',
            color = 0x2ecc71
        )
        embed.set_image(url="https://i.ytimg.com/vi/F_e2eknfMbU/hqdefault.jpg")
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await welcome.send(embed=embed)


async def setup(client):
    await client.add_cog(welcome(client))