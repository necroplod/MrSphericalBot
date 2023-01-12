import discord
from discord.ext import commands

class info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["Help", "hELP", "HELP"])
    async def help(self, ctx):
      emb = discord.Embed(title = 'ДОСТУПНЫЕ КОМАНДЫ:', description = ' ', colour = discord.Color.red())
      emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
      emb.add_field(name = 'Информация', value = f'`c.help` `c.stats`', inline=False)
      emb.add_field(name = 'Веселье', value = f'`c.catkdk`', inline=False)
      await ctx.send(embed=emb)

    @commands.command()
    async def stats(self, ctx):
        name = ctx.guild.name
        servid = ctx.guild.id
        member = ctx.guild.member_count
        owner = ctx.guild.owner
        emoji = len(ctx.guild.emojis)
        created_at = ctx.guild.created_at.strftime("Дата: %d/%m/%Y Время: %H:%M:%S %p")
        txtchs = len(ctx.guild.text_channels)
        vcchs = len(ctx.guild.voice_channels)
        lvlboost = f'{ctx.guild.premium_subscription_count}'
        role_num = len(ctx.guild.roles)
        allrole = [item.name for item in ctx.guild.roles]
        allrole.pop(0)
        role = ctx.guild.get_role(952530469700911119)
        verify_count = ctx.guild.member_count - len(role.members)
        emd = discord.Embed(title='**Информация:**')
        emd.add_field(name="Название Сервера", value=f'```\n{name}```', inline=True)
        emd.add_field(name="Владелец", value=f'```\n{owner}```', inline=True)
        emd.add_field(name="Количество Участников", value=f'```\n{member}```', inline=False)
        emd.add_field(name="ID Сервера", value=f'```\n{servid}```', inline=True)
        emd.add_field(name="Количество Эмодзи", value=f'```\n{emoji}```', inline=False)
        emd.add_field(name="Дата Создания", value=f'```\n{created_at}```', inline=False)
        emd.add_field(name="Количество Ролей", value=f'```\n{role_num}```', inline=False)
        emd.add_field(name="Количество Текстовых Каналов", value=f'```\n{txtchs}```', inline=False)
        emd.add_field(name="Количество Голосовых Каналов", value=f'```\n{vcchs}```', inline=False)
        emd.add_field(name="Количество бустов сервера", value=f'```\n{lvlboost}```', inline=False)
        emd.add_field(name="Количество участников не прошедших верификацию", value=f'```\n{verify_count}```', inline=False)

        await ctx.send(embed=emd)


def setup(client):
    client.add_cog(info(client))