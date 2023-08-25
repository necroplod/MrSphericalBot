import datetime
import discord
from discord.ext import commands

import settings

class welcome(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        guild = self.client.get_guild(settings.misc.guild)
        global invites
        invites = await guild.invites()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        r = member.guild.get_role(997425505349419099)
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
                    description=f'''●──────────────────────────────────●\n{member.mention} — ***{member.name}***\n●──────────────────────────────────●\nБот был добавлен {inviter.mention}''',
                    color = 0x2ecc71,
                    timestamp = datetime.datetime.now()
                )
            else:
                def invite(lst, code):
                    for invt in lst:
                        if invt.code == code:
                            return invt.uses
                invb = invites[0]
                inva = await member.guild.invites()
                try:
                    for inv in invb:
                        if inv.uses < invite(inva, inv.code):
                            inviter = inv.inviter.id
                            uses = inv.uses + 1

                    embed = discord.Embed(
                        title='',
                        description=f'''●──────────────────────────────────●\n{member.mention} — ***{member.name}***\n●──────────────────────────────────●\n*Пламенный привет тебе друг!\nЗаваривай кофеёк, и залетай в наилучший сервер на свете!\n\nЕго пригласил <@{inviter}>, который теперь пригласил **{uses}** участников*''',
                        color = 0x2ecc71,
                        timestamp = datetime.datetime.now()
                    )
                    await member.add_roles(r)
                except:
                    embed = discord.Embed(
                        title='',
                        description=f'''●──────────────────────────────────●\n{member.mention} — ***{member.name}***\n●──────────────────────────────────●\n*Пламенный привет тебе друг!\nЗаваривай кофеёк, и залетай в наилучший сервер на свете!\n\nОн использовал персональную ссылку сервера.*''',
                        color = 0x2ecc71,
                        timestamp = datetime.datetime.now()
                    )
                    await member.add_roles(r)

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
            description=f'''●──────────────────────────────────●\n{member.mention} — ***{member.name}***\n●──────────────────────────────────●\n***Покинул нас.***''',
            color = 0x2ecc71,
            timestamp = datetime.datetime.now()
        )
        embed.set_image(url="https://i.ytimg.com/vi/F_e2eknfMbU/hqdefault.jpg")
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await welcome.send(embed=embed)
        invites[0] = await member.guild.invites()


async def setup(client):
    await client.add_cog(welcome(client))