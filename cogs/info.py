import discord
import typing
import settings
from discord.ext import commands
from discord import app_commands
from typing import Union, Literal, Optional

prefix = '/'



class info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @app_commands.command(name = "help", description = "Получите список команд")
    async def help(
            self, interaction: discord.Interaction
    ):
      embed = discord.Embed(
          title = '📚 | Доступные Команды',
          description = '',
          colour = discord.Color.red()
      )

      embed.add_field(name = '<:pakistan:1046443315177984130>  Информация', value = f'`{prefix}help` `{prefix}alarm`', inline=False)
      embed.add_field(name = '<:moon:1051616411971231804>  Веселье', value = f'`{prefix}catkdk` `{prefix}kdk` `{prefix}kdkeat`', inline=False)
      embed.add_field(name = '<:canada:1071734769395716116>  Стикеры', value = f'`{prefix}лох` `{prefix}украина` `{prefix}да` `{prefix}эй` `{prefix}бомба` `{prefix}осуждаю` `{prefix}быдло` `{prefix}стоп` `{prefix}кринж` `{prefix}господин`', inline = False)
      embed.add_field(name = '<:kazahstan:1051609522642374727>  Розыгрыши и прочее', value = f'`{prefix}giveaway` `{prefix}poll`', inline=False)
      embed.add_field(name = '<:king:1005355877278154814>  Админские Штучки', value = f'`{prefix}art` `{prefix}archive` `s.ticket` `{prefix}proof`', inline=False)
      embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')

      await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "alarm", description = "Оповестите модерацию о нарушении")
    async def alarm(
            self, interaction: discord.Interaction,
            нарушитель: Union[discord.Member],
            канал: Union[discord.TextChannel],
            причина: str

    ):
        modchat = self.client.get_channel(settings.channels.mod_chat)
        embed = discord.Embed(
            title='🦺 | Вызов модерации',
            description=f'''
            **• Пользователь:** <@{interaction.user.id}> | `{interaction.user.id}`
            **• Канал:** <#{канал.id}>

            **• Нарушитель:** <@{нарушитель.id}>
            **• Причина:** `{причина}`''',
            color=0xff6565
        )
        embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
        answer = discord.Embed(
            title='🦺 | Вызов модерации',
            description=f'<a:768563657390030971:1041076662546219168> <@{interaction.user.id}>, Вызов модерации успешно выполнен! Скоро они прибут на помощь и решат данную ситуацию.',
            color=0xff6565
        )
        answer.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
        await interaction.response.send_message(embed=answer)
        await modchat.send('<@&1052168161304260629>', embed=embed)
async def setup(client):
    await client.add_cog(info(client))