import discord
import datetime
import settings
from config import Panel
from discord.ext import commands
from discord.ui.view import View
from discord.ui.modal import Modal

class auth_panel(Modal, title = '🎆 | Аутентификация'):
    login = discord.ui.TextInput(
        label = 'Логин',
        placeholder = 'KrytoyAdmin2009 :)'
    )
    pwd = discord.ui.TextInput(
        label = 'Пароль',
        placeholder = 'qwerty123456'
    )
    async def on_submit(self, interaction: discord.Interaction):
        if self.login.value == Panel.login:
            if self.pwd.value in Panel.pwds:
                logs = discord.utils.get(interaction.guild.channels, name=settings.channels.logs_name)
                embed = discord.Embed(
                    title='🎲 | Панель Управления',
                    description=f'''
                    **• Действие:** Авторизация
                    **• Администратор:** <@{interaction.user.id}>
                    **• Время:** {datetime.datetime.now()}''',
                    color=0xcdc9a5
                )
                embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
                await logs.send(embed=embed)
                embed = discord.Embed(
                    title='🎲 | Панель Управления',
                    description='',
                    color=0xcdc9a5
                )
                embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
                await interaction.response.send_message(embed=embed, view = main_panel())
            else:
                await interaction.response.send_message('Неверный пароль!')
        else:
            await interaction.response.send_message('Неверный логин!')
class cogs_panel(Modal, title = '🎲 | Панель управления'):
    cog = discord.ui.TextInput(label = 'Имя кога')
    action = discord.ui.TextInput(
        label = 'Действие',
        placeholder = 'Действия: load, unload, reload')
    async def on_submit(self, interaction: discord.Interaction):
        cog = f'cogs.{self.cog.value}'
        action = self.action.value
        action = action.lower()
        if action == 'load':
            async def cogs_():
                await discord.ext.commands.Botload_extension(name = cog)
        if action == 'reload':
            async def cogs_():
                await discord.ext.commands.Bot.unload_extension(name = cog)
                await discord.ext.commands.Botload_extension(name = cog)
        if action == 'unload':
            async def cogs_():
                await discord.ext.commands.Bot.unload_extension(name = cog)
class bans_panel(Modal, title = '🎲 | Панель управления'):
    one = discord.ui.TextInput(label = 'ID')
    two = discord.ui.TextInput(label = 'ID')
    three = discord.ui.TextInput(label = 'ID')
    four = discord.ui.TextInput(label = 'ID')
    reason = discord.ui.TextInput(label = 'Причина')
    async def on_submit(self, interaction: discord.Interaction):
        bans = list([])
        bans.append(self.one.value)
        bans.append(self.two.value)
        bans.append(self.three.value)
        bans.append(self.four.value)
        logs = discord.utils.get(interaction.guild.channels, name=settings.channels.punishments_name)
        for id in bans:
            async def ban_():
                usr = discord.ext.commands.Bot.get_user(id)
                await discord.Guild.ban(user = usr,
                                        reason = f'{self.reason.value} | {interaction.user.name}#{interaction.user.discriminator}')
                embed = discord.Embed(
                    title = '🎯 | Наказания',
                    description = f'''<a:768563657390030971:1041076662546219168> **Участник <@&{id}> был забанен.**
                    <a:768563657390030971:1041076662546219168> **Модератор:** <@&{interaction.user.id}>
                    <a:768563657390030971:1041076662546219168> **Причина:** {self.reason.value}''',
                    color = 0xea6363
                )
                embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
                await logs.send(embed=embed)

class main_panel(discord.ui.View):
    def __init__(self, *, timeout=10):
        super().__init__(timeout=timeout)

    @discord.ui.button(emoji='🪁', style=discord.ButtonStyle.green, label = 'Управлять когами', row = 1)
    async def cogs(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(cogs_panel())

    @discord.ui.button(emoji='🦺', style=discord.ButtonStyle.green, label = 'Бан пользователей', row = 1)
    async def bans(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(bans_panel())

class auth_start(discord.ui.View):
    def __init__(self, *, timeout=60):
        super().__init__(timeout=timeout)

    @discord.ui.button(emoji='🥊', style=discord.ButtonStyle.blurple, label = 'Авторизация')
    async def auth(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(auth_panel())
class panel(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role(952530469751255043, 952530469751255042)
    async def panel(self, ctx):
        embed = discord.Embed(
            title = '🎲 | Панель Управления',
            description = '<a:768563657390030971:1041076662546219168> **Пройдите авторизацию..**',
            color = 0xcdc9a5
        )
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed, view = auth_start())

async def setup(client):
    await client.add_cog(panel(client))
