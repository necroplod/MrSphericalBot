import discord
import typing
import settings
from discord.ext import commands
from discord.ui.view import View
from discord.ui.modal import Modal

prefix = 's.'

class Alarm_arguments(Modal, title = '🦺 | Вызов модерации'):
    reason = discord.ui.TextInput(
        label = 'Причина:'
    )
    usr = discord.ui.TextInput(
        label = 'Нарушитель:',
        placeholder = 'ID или ник нарушителя, если такой есть. Если его нет, то оставьте это поле пустым!',
        required = False
    )
    async def on_submit(self, interaction: discord.Interaction):
        modchat = discord.utils.get(interaction.guild.channels, name=settings.channels.mod_chat)
        this = discord.utils.get(interaction.guild.channels, name=interaction.channel.name)
        if self.usr.value is None:
            offender = 'Не указан'
        if self.usr.value == '':
            offender = 'Не указан'
        if self.usr.value == ' ':
            offender = 'Не указан'
        else:
            offender = self.usr.value


        embed = discord.Embed(
            title = '🦺 | Вызов модерации',
            description = f'''
            **• Пользователь:** <@{interaction.user.id}> | `{interaction.user.id}`
            **• Канал:** <#{interaction.channel.id}>
            
            **• Нарушитель:** `{offender}`
            **• Причина:** `{self.reason.value}`''',
            color = 0xff6565
        )
        embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
        answer = discord.Embed(
            title = '🦺 | Вызов модерации',
            description = f'<a:768563657390030971:1041076662546219168> <@{interaction.user.id}>, Вызов модерации успешно выполнен! Скоро они прибут на помощь и решат данную ситуацию.',
            color=0xff6565
        )
        answer.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
        await modchat.send('<@&1052168161304260629>', embed=embed)
        await interaction.response.send_message(embed=answer)
class Alarm(discord.ui.View):
    def __init__(self, *, timeout=30, author):
        self.author = author
        super().__init__(timeout=timeout)

    @discord.ui.button(emoji='📢', label = 'Вызов', style=discord.ButtonStyle.red)
    async def start(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.author:
            await interaction.response.send_message(content="Эта кнопка была вызвана другим пользователем!", ephemeral=True)
        await interaction.response.send_modal(Alarm_arguments())


class info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
      embed = discord.Embed(
          title = '📚 | Доступные Команды',
          description = '',
          colour = discord.Color.red()
      )
      embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar.url)

      embed.add_field(name = '<:pakistan:1046443315177984130>  Информация', value = f'`{prefix}help` `{prefix}alarm`', inline=False)
      embed.add_field(name = '<:moon:1051616411971231804>  Веселье', value = f'`{prefix}catkdk` `{prefix}kdk` `{prefix}kdkeat`', inline=False)
      embed.add_field(name = '<:serbia:1051616011272589452>  ВПИ', value = f'`{prefix}msg`', inline=False)
      embed.add_field(name = '<:kazahstan:1051609522642374727>  Розыгрыши и прочее', value = f'`{prefix}giveaway` `{prefix}reroll` `{prefix}poll`', inline=False)
      embed.add_field(name = '<:king:1005355877278154814>  Админские Штучки', value = f'`{prefix}art` `{prefix}archive` `{prefix}panel`', inline=False)
      embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
      await ctx.send(embed=embed)

    @commands.command()
    async def alarm(self, ctx):
        embed = discord.Embed(
            title = '🦺 | Вызов модерации',
            description = '<a:768563657390030971:1041076662546219168> **Произошло нарушение правил? Вызовите модерацию!**',
            color = 0xff6565
        )
        embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
        await ctx.send(embed=embed, view = Alarm(author = ctx.author))
async def setup(client):
    await client.add_cog(info(client))