import discord
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
            **• Причина:** `{self.reason.value}`
            **• Нарушитель:** `{offender}`''',
            color = 0xff6565
        )
        await modchat.send('<@&1052168161304260629>', embed=embed)
class Alarm(discord.ui.View):
    def __init__(self, *, timeout=30):
        super().__init__(timeout=timeout, )

    @discord.ui.button(emoji='📢', label = 'Вызов', style=discord.ButtonStyle.red)
    async def start(self, interaction: discord.Interaction, button: discord.ui.Button):
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

      embed.add_field(name = '<:khrushchev:1005361978442780680>  Информация', value = f'`{prefix}help`', inline=False)
      embed.add_field(name = '<:earch:1005361448513445888>  Веселье', value = f'`{prefix}catkdk` `{prefix}kdk` `{prefix}kdkeat`', inline=False)
      embed.add_field(name = '<:king:1005355877278154814>  Админские Штучки', value = f'`{prefix}giveaway` `{prefix}reroll` `{prefix}art` `{prefix}archive`', inline=False)
      embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
      await ctx.send(embed=embed)

    @commands.command()
    async def alarm(self, ctx):
        embed = discord.Embed(
            title = '🦺 | Вызов модерации',
            description = '<a:768563657390030971:1041076662546219168> **Произошло нарушение правил? Вызовите модерацию!**',
            color = 0xff6565
        )
        await ctx.send(embed=embed, view = Alarm())
async def setup(client):
    await client.add_cog(info(client))