import settings
import discord
import typing
from pymongo import MongoClient
from discord.ext import commands
from discord import app_commands
from config.config import mongoconf
import settings
import datetime

cluster = MongoClient(mongoconf.uri)
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
        logs = self.client.get_channel(settings.logs.event)
        role = interaction.guild.get_role(settings.roles.eventor)
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
                    description=f"***Чат был открыт ивентором <@{interaction.user.id}>***",
                    color=0xd09248
                )
                embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
                await ch.set_permissions(rolemembers, read_messages=True, send_messages=True)

                embed2 = discord.Embed(
                    title="🎀 | Ивенты",
                    description=f">>> Чат ивентов открыт.",
                    color=0xd09248
                )
                embed2.add_field(name="Ивентор:", value=f"<@{interaction.user.id}> ({interaction.user.id})", inline=True)
                embed2.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
                await logs.send(embed=embed2)
            if действие == 'закрыть':
                embed = discord.Embed(
                    title="🎀 | Ивенты",
                    description=f"***Чат был закрыт ивентором <@{interaction.user.id}>***\n\n***До скорых встреч!***",
                    color=0xd09248
                )
                embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
                await ch.set_permissions(rolemembers, read_messages=True, send_messages=False)

                embed2 = discord.Embed(
                    title="🎀 | Ивенты",
                    description=f">>> Чат ивентов закрыт.",
                    color=0xd09248
                )
                embed2.add_field(name="Ивентор:", value=f"<@{interaction.user.id}> ({interaction.user.id})", inline=True)
                embed2.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)


            await ch.send(embed=embed)
            await logs.send(embed=embed2)
            await interaction.response.send_message('*Готово!*', ephemeral=True)

    @app_commands.command(name = "topmanage", description = "Управление топом победителей")
    async def topmanage(
            self, interaction: discord.Interaction,
            действие: typing.Literal['добавить', 'убавить', 'очистить'],
            участник: discord.User,
            число: typing.Optional[int]
    ):
        logs = self.client.get_channel(settings.logs.event)
        role = interaction.guild.get_role(settings.roles.eventor)
        fnd = {'_id': участник.id}
        avanturist = interaction.guild.get_role(settings.roles.avanturist)
        traveler = interaction.guild.get_role(settings.roles.traveler)
        firstevent = interaction.guild.get_role(settings.roles.firstevent)
        if участник.id is None or число is None: await interaction.response.send_message(f'*Недостаточно аргументов команды!*', ephemeral=True)
        if role not in interaction.user.roles: await interaction.response.send_message('*У Вас недостаточно прав! Вам необходимо иметь роль <@&1142038601220235314>*', ephemeral=True)
        elif role in interaction.user.roles:
            if число < 1 and действие != 'очистить': await interaction.response.send_message(f'*Число **{число}** меньше единицы!*', ephemeral=True)

            if действие == 'добавить':
                if collect.count_documents(fnd) == 1:
                    cnt = collect.find_one(fnd)['count']
                    collect.update_one(fnd, {'$set': {'count': cnt + число}})
                    if cnt + число == 3:
                        if traveler not in участник.roles:
                            await участник.add_roles(traveler)
                    if cnt + число == 5:
                        if firstevent not in участник.roles:
                            await участник.add_roles(firstevent)
                elif collect.count_documents(fnd) == 0:
                    collect.insert_one({'_id': участник.id, 'count': число})
                    if avanturist not in участник.roles:
                        await участник.add_roles(avanturist)

                embed = discord.Embed(
                    title="🎇 | Доска победителей",
                    description=f">>> Увеличено число побед <@{участник.id}> на **{число}**!",
                    color=0xfaa821
                )
                embed.add_field(name="Ивентор:", value=f"<@{interaction.user.id}> ({interaction.user.id})", inline=True)
                embed.add_field(name="Участник:", value=f"<@{участник.id}> ({участник.id})", inline=True)
                embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
                await logs.send(embed=embed)
                await interaction.response.send_message(f'*Вы успешно добавили участнику <@{участник.id}> **{число}** побед!*')
                await участник.send(f'*Поздравляю, {участник.mention}! Твоё остроумие и настойчивость принесли результаты. Продолжай в том же духе!*')
            if действие == 'убавить':
                if collect.count_documents(fnd) == 1:
                    cnt = collect.find_one(fnd)['count']
                    if число > cnt: число = cnt
                    if число <= cnt: 
                        collect.delete_one(fnd) 
                    else:
                        collect.update_one(fnd, {'$set': {'count': cnt - число}})
                    embed = discord.Embed(
                            title="🎇 | Доска победителей",
                            description=f">>> Уменьшено число побед <@{участник.id}> на **{число}**!",
                            color=0xfaa821
                     )
                    embed.add_field(name="Ивентор:", value=f"<@{interaction.user.id}> ({interaction.user.id})", inline=True)
                    embed.add_field(name="Участник:", value=f"<@{участник.id}> ({участник.id})", inline=True)
                    embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
                    await logs.send(embed=embed)
                    await interaction.response.send_message(f'*Вы успешно убавили количество побед участника <@{участник.id}> на **{число}***')
                if collect.count_documents(fnd) == 0: await interaction.response.send_message(f'*Участника <@{int(участник.id)}> нету в базе данных, Вы не можете уменьшить число побед!*')

            if действие == 'очистить':
                role2 = interaction.guild.get_role(1142038902211870730)
                if role2 not in interaction.user.roles: await interaction.response.send_message('*У Вас недостаточно прав! Вам необходимо иметь роль <@&1142038902211870730>*', ephemeral=True)
                if role2 in interaction.user.roles:
                    for member in interaction.guild.members:
                        if avanturist in member.roles:
                            await member.remove_roles(avanturist)
                        if traveler in member.roles:
                            await member.remove_roles(traveler)
                        if firstevent in member.roles:
                            await member.remove_roles(firstevent)
                    collect.delete_many({})
                    embed = discord.Embed(
                        title="🎇 | Доска победителей",
                        description=f">>> Очищена доска победителей!",
                        color=0xfaa821
                    )
                    embed.add_field(name="Куратор:", value=f"<@{interaction.user.id}> ({interaction.user.id})", inline=True)
                    embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
                    await logs.send(embed=embed)
                    await interaction.response.send_message(f'*Вы успешно очистили доску победителей*!')



    @app_commands.command(name="evtop", description="Просмотр топа победителей")
    async def evtop(
            self, interaction: discord.Interaction
    ):
        lst = []
        number = [2, 3, 4]
        top_players = collect.find().sort("count", -1).limit(10)
        for index, query in enumerate(top_players):
            if query['count'] == 1: txt = "победа"
            if query['count'] in number: txt = "победы"
            if query['count'] >= 5: txt = "побед"
            if query['count'] == 0: txt = "побед"
            match index + 1:
                case 1:
                    lst.append(f'<a:768563657390030971:1041076662546219168>  🏆 ***{index + 1}*** — <@{query["_id"]}> — `{query["count"]}` {txt}')
                case 2:
                    lst.append(f'<a:768563657390030971:1041076662546219168>  🪐 ***{index + 1}*** — <@{query["_id"]}> — `{query["count"]}` {txt}')
                case 3:
                    lst.append(f'<a:768563657390030971:1041076662546219168>  🌎 ***{index + 1}*** — <@{query["_id"]}> — `{query["count"]}` {txt}')
                case _:
                    lst.append(f'<a:768563657390030971:1041076662546219168>  ***{index + 1}*** — <@{query["_id"]}> — `{query["count"]}` {txt}')
        embed = discord.Embed(
            description = "\n".join(lst),
            color = 0x8f00ff
        )
        embed.set_footer(icon_url=settings.misc.avatar_url, text="Это топ победителей участвующих в ивентах. Рады для вас их проводить ;)")
        await interaction.response.send_message(content = "# 🎇 | Доска победителей", embed=embed)













        
async def setup(client):
    await client.add_cog(events(client))
