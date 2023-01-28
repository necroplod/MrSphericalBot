import datetime

import settings

import discord
from discord.ext import commands

class welcome(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == settings.misc.guild:
            welcome = self.client.get_channel(settings.channels.welcome)

            if member.bot:
                integrations = await member.guild.integrations()
                for integration in integrations:
                    if isinstance(integration, discord.BotIntegration):
                        if integration.application.user.name == member.name:
                            inviter = integration.user
                embed = discord.Embed(
                    title='',
                    description=f'''
                    ●─────────────────●
                    {member.mention}
                    ●─────────────────● 
                    Бот был добавлен {inviter.mention}''',
                    color = 0x2ecc71,
                    timestamp = datetime.datetime.now()
                )
            else:
                embed = discord.Embed(
                    title='',
                    description=f'''
                    ●─────────────────●
                    {member.mention}
                    ●─────────────────● 
                    *Пламенный привет тебе друг!
                    Заваривай кофеёк, и залетай в наилучший сервер на свете!*''',
                    color = 0x2ecc71,
                    timestamp = datetime.datetime.now()
                )

            embed.set_image(url="https://i.ytimg.com/vi/nVzqh0fTARU/hqdefault.jpg")
            embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
            await welcome.send(embed=embed)
        else:
            return

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        welcome = self.client.get_channel(settings.channels.welcome)
        embed = discord.Embed(
            title='',
            description=f'''
            ●─────────────────●
            {member.mention}
            ●─────────────────●
            **Покинул нас.**''',
            color = 0x2ecc71,
            timestamp = datetime.datetime.now()
        )
        embed.set_image(url="https://i.ytimg.com/vi/F_e2eknfMbU/hqdefault.jpg")
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await welcome.send(embed=embed)


async def setup(client):
    await client.add_cog(welcome(client))