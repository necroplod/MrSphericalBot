import settings
import discord
import typing
from pymongo import MongoClient
from discord.ext import commands
from discord import app_commands
from config.config import mongoconf

cluster = MongoClient(f"{mongoconf.uri}")
db = cluster.db
collect = db.event

class events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @app_commands.command(name="evmanage", description="Управляйте чатом иветов")
    async def eventmanage(
            self, interaction: discord.Interaction,
            действие: typing.Literal['открыть', 'закрыть']
    ):
        role = interaction.guild.get_role(1142038601220235314)
        ch = interaction.guild.get_channel(1142025152398376980)
        rolemembers = interaction.guild.get_role(1146028746680311839)

        if role not in interaction.user.roles:
            await interaction.response.send_message(
                '*У Вас недостаточно прав! Вам необходимо иметь роль <@&1142038601220235314>*', ephemeral=True)
            return
        elif role in interaction.user.roles:
            if действие == 'открыть':
                embed = discord.Embed(
                    title="🎀 | Ивенты",
                    description=f"***Чат был открыт ивентором <@{interaction.user.id}>***\n\n***До скорых встреч!***",
                    color=0xd09248
                )
                embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
                await ch.set_permissions(rolemembers, read_messages=True, send_messages=True)
            if действие == 'закрыть':
                embed = discord.Embed(
                    title="🎀 | Ивенты",
                    description=f"***Чат был закрыт ивентором <@{interaction.user.id}>***",
                    color=0xd09248
                )
                embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
                await ch.set_permissions(rolemembers, read_messages=True, send_messages=False)

            await ch.send(embed=embed)
            await interaction.response.send_message('*Готово!*', ephemeral=True)

    @app_commands.command(name = "topmanage", description = "Управление топом победителей")
    async def topmanage(
            self, interaction: discord.Interaction,
            действие: typing.Literal['добавить', 'убавить'],
            айди: typing.Optional[str],
            число: typing.Optional[int]
    ):
        role = interaction.guild.get_role(1142038601220235314)
        fnd = {'_id': айди}

        if айди is None or число is None: await interaction.response.send_message(f'*Недостаточно аргументов команды!*', ephemeral=True)
        if role not in interaction.user.roles: await interaction.response.send_message('*У Вас недостаточно прав! Вам необходимо иметь роль <@&1142038601220235314>*', ephemeral=True)
        elif role in interaction.user.roles:
            if число < 1: await interaction.response.send_message(f'*Число **{число}** меньше единицы!*', ephemeral=True)

            if действие == 'добавить':
                if collect.count_documents(fnd) == 1:
                    cnt = collect.find_one(fnd)['count']
                    collect.update_one(fnd, {'$set': {'count': cnt + число}})
                elif collect.count_documents(fnd) == 0:
                    collect.insert_one({'_id': айди, 'count': число})
                await interaction.response.send_message(f'*Вы успешно добавили участнику <@{int(айди)}> **{число}** побед!*')
            if действие == 'убавить':
                if collect.count_documents(fnd) == 0: await interaction.response.send_message(f'*Участника <@{int(айди)}> нету в базе данных, Вы не можете уменьшить число побед!*')
                if collect.count_documents(fnd) == 1:
                    cnt = collect.find_one(fnd)['count']
                    if число > cnt: await interaction.response.send_message(f'*Число **{число}** больше чем число побед!*', ephemeral=True)
                    else:
                        collect.update_one(fnd, {'$set': {'count': cnt - число}})
                        await interaction.response.send_message(f'*Вы успешно убавили количество побед участника <@{int(айди)}> на **{число}***')


    @app_commands.command(name="evtop", description="Просмотр топа победителей")
    async def evtop(
            self, interaction: discord.Interaction
    ):
        lst = []
        for query in collect.find():
            if query['count'] == 1: txt = "победа"
            if query['count'] != 1: txt = "побед"

            lst.append(f'<a:1041076662546219168:1041076662546219168> <@{query["_id"]}> — ***{query["count"]}*** {txt}')

        embed = discord.Embed(
            title = "🎇 | Доска победителей",
            description = "\n".join(lst),
            color = 0xfaa821
        )
        embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)

        await interaction.response.send_message(embed=embed)













        
async def setup(client):
    await client.add_cog(events(client))
