import discord
import typing
import settings
from discord.ext import commands
from discord import app_commands
from typing import Union, Literal, Optional

prefix = '/'

class VerifyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(emoji='🎳', style=discord.ButtonStyle.green, label = 'Верификация', custom_id = "verify:verify")
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = interaction.guild.get_role(settings.roles.toxic)
        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f'*Роль <@&{role.id}> успешно выдана!*', ephemeral = True)
        else:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f'*Роль <@&{role.id}> успешно убрана!*', ephemeral=True)

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
      #embed.add_field(name = '<:moon:1051616411971231804>  Веселье', value = f'`{prefix}catkdk` `{prefix}kdk` `{prefix}kdkeat`', inline=False)
      embed.add_field(name = '<:nasa:1063562901958438922>    RP-Команды', value = f'`{prefix}kiss` `{prefix}hug` `{prefix}pat` `{prefix}slap` `{prefix}feed` `{prefix}cry` `{prefix}tickle` `{prefix}bite` `{prefix}sleep` `{prefix}eat` `{prefix}angry` `{prefix}kill` `{prefix}shy` `{prefix}shake` `{prefix}lick` `{prefix}relax` `{prefix}flex` `{prefix}hi` `{prefix}bye`', inline=False)
      embed.add_field(name = '<:king:1005355877278154814>  Админские Штучки', value = f'`{prefix}art` `{prefix}artmany` `{prefix}poll` `s.role` `s.ticket` `{prefix}proof` `{prefix}recruit`', inline=False)
      embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')

      await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "alarm", description = "Оповестите модерацию о нарушении")
    async def alarm(
            self, interaction: discord.Interaction,
            нарушитель: Union[discord.Member],
            канал: Union[discord.TextChannel],
            причина: str

    ):
        mod = self.client.get_channel(settings.channels.mod_notify)
        embed = discord.Embed(
            title='🦺 | Вызов модерации',
            description=f'''<a:768563657390030971:1041076662546219168>  Пользователь: <@{interaction.user.id}> | `{interaction.user.id}`\n<a:768563657390030971:1041076662546219168>  Канал: <#{канал.id}>\n<a:768563657390030971:1041076662546219168>  Нарушитель: <@{нарушитель.id}>\n<a:768563657390030971:1041076662546219168>  Причина: `{причина}`''',
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
        await mod.send(f'<@&1102489864240373811>', embed=embed)

    """
    @commands.command()
    @commands.has_any_role(1071141626866569286)
    async def verify(self, ctx):
        embed = discord.Embed(
            title = "🎇 | Верификация",
            description = f"<a:768563657390030971:1041076662546219168> Всё, что вы увидели в чатах, которые станут вам доступны, должно остаться там. Никакого распространения скринов из этого чата или любой другой информации.",
            color = 0x7b7385
        )
        embed.set_footer(icon_url=self.client.user.avatar.url, text=f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed, view = VerifyView())"""



async def setup(client):
    await client.add_cog(info(client))