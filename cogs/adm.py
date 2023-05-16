import settings
import datetime
import discord
import asyncio
import random
import re
from discord.ext import commands
from discord.ui.view import View
from discord.ui.modal import Modal
from discord import app_commands
from typing import Union, Literal, Optional


class adm(commands.Cog):

    def __init__(self, client):
        self.client = client


    @app_commands.command(name = "art", description = "Сохраните арт в архив!")
    async def art(
            self, interaction: discord.Interaction,
            айди: str
    ):
        role = interaction.guild.get_role(1071139216580419644)

        if role not in interaction.user.roles:
            await interaction.response.send_message('*У Вас недостаточно прав! Вам необходимо иметь роль <@&1071139216580419644>*', ephemeral = True)
            return
        elif role in interaction.user.roles:

            general_art = discord.utils.get(interaction.guild.channels, id=settings.channels.art)
            archive_art = discord.utils.get(interaction.guild.channels, id=settings.channels.archive_art)
            msg = await general_art.fetch_message(int(айди))
            attachment = msg.attachments[0]

            embed = discord.Embed(
                title="",
                description="",
                timestamp=msg.created_at,
                color=msg.author.color
            )
            embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
            embed.set_author(name=f"Арт от {msg.author.display_name}", icon_url=msg.author.avatar.url)
            embed.set_image(url=f"{attachment.url}")
            await archive_art.send(embed=embed)
            await interaction.response.send_message('*Готово!*', ephemeral=True)

    @app_commands.command(name="giveaway", description="Проведите розыгрыш")
    async def giveaway(
            self, interaction: discord.Interaction,
            канал: Union[discord.TextChannel],
            победителей: int,
            время: str,
            приз: str
    ):
        role = interaction.guild.get_role(1071139413586882652)

        if role not in interaction.user.roles:
            await interaction.response.send_message('*У Вас недостаточно прав! Вам необходимо иметь роль <@&1071139413586882652>*', ephemeral = True)
            return
        elif role in interaction.user.roles:
            if not канал.permissions_for(interaction.guild.me).send_messages or not канал.permissions_for(interaction.guild.me).add_reactions:
                return await interaction.response.send_message(f"У бота нет правильных разрешений для отправки: <#{канал.id}\n ** Необходимые разрешения: ** ``Добавлять реакции | Отправлять сообщения``.")

            seconds = ("s", "sec", "c", 'сек')
            minutes = ("m", "min", "м", "мин")
            hours = ("h", "hour", "ч", "час")
            days = ("d", "day", "д", "дней")
            weeks = ("w", "week", "нед", "недель")
            rawsince = время
            since = время
            try:
                temp = re.compile("([0-9]+)([a-zA-Z]+)")
                if not temp.match(since):
                    return await interaction.response.send_message("Вы не указали единицу времени, пожалуйста, повторите попытку.", ephemeral = True)
                res = temp.match(since).groups()
                time = int(res[0])
                since = res[1]
            except:
                return await interaction.response.send_message("Вы не указали единицу времени, пожалуйста, повторите попытку.")

            if since.lower() in seconds:
                timewait = time
            elif since.lower() in minutes:
                timewait = time * 60
            elif since.lower() in hours:
                timewait = time * 3600
            elif since.lower() in days:
                timewait = time * 86400
            elif since.lower() in weeks:
                timewait = time * 604800
            else:
                return await interaction.response.send_message("Вы не указали единицу времени, пожалуйста, повторите попытку.", ephemeral = True)

            futuredate = datetime.datetime.utcnow() + datetime.timedelta(seconds=timewait)
            embed1 = discord.Embed(
                color=discord.Color(random.randint(0x000000, 0xFFFFFF)),
                title=f"🎉 | РОЗЫГРЫШ\n`{приз}`", timestamp=futuredate,
                description=f'Нажмите на 🎉 чтобы вступить!\nСоздан: <@{interaction.user.id}>'
            )
            embed1.set_footer(text=f"Розыгрыш закончится")
            msg = await канал.send(embed=embed1)
            await msg.add_reaction("🎉")

            await asyncio.sleep(timewait)
            message = await канал.fetch_message(msg.id)
            for reaction in message.reactions:
                if str(reaction.emoji) == "🎉":
                    users = [user async for user in reaction.users()]
                    if len(users) == 1:
                        return await msg.edit(embed=discord.Embed(title="Никто не выиграл в розыгрыше."))
            try:
                winners = random.sample([user for user in users if not user.bot], k=победителей)
            except ValueError:
                return await канал.send("Недостаточно участников")
            winnerstosend = "\n".join([winner.mention for winner in winners])

            win = await msg.edit(
                embed=discord.Embed(title="🎉 | ПОБЕДИТЕЛЬ",
                description=f"Поздравляем {winnerstosend}, вы выиграли **{приз}**!",
                color=discord.Color.blue())
            )

    @app_commands.command(name = "poll", description = "Создайте опрос")
    async def poll(
            self, interaction: discord.Interaction,
            тема: str,
            канал: Union[discord.TextChannel],
            вариант1: str,
            вариант2: str,
            вариант3: str,
            вариант4: str,
            вариант5: str

    ):
        role = interaction.guild.get_role(1071139871105744977)

        if role not in interaction.user.roles:
            await interaction.response.send_message('*У Вас недостаточно прав! Вам необходимо иметь роль <@&1071139871105744977>*', ephemeral = True)
            return
        elif role in interaction.user.roles:
            one = f":one: {вариант1}"
            two = f":two: {вариант2}"
            three = f":three: {вариант3}"
            four = f":four: {вариант4}"
            five = f":five: {вариант5}"


            embed = discord.Embed(
                title='🎁 | Опрос',
                description=f"""**{тема}**\n{one}\n{two}\n{three}\n{four}\n{five}
            """,
                color=0x007f5c
            )
            embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
            embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar)

            msg = await канал.send(f'<@&{settings.roles.poll_role}>', embed=embed)

            await msg.add_reaction('1️⃣')
            await msg.add_reaction('2️⃣')
            await msg.add_reaction('3️⃣')
            await msg.add_reaction('4️⃣')
            await msg.add_reaction('5️⃣')


    @app_commands.command(name = "proof", description = "Отправьте доказательства")
    async def proof(
            self, interaction: discord.Interaction,
            нарушитель: Union[discord.Member],
            время: str,
            file: discord.Attachment
        ):
        role = interaction.guild.get_role(1103258122736369675)

        if role not in interaction.user.roles:
            await interaction.response.send_message('*У Вас недостаточно прав! Вам необходимо иметь роль <@&1103258122736369675>*', ephemeral = True)
            return
        elif role in interaction.user.roles:
            ch = self.client.get_channel(settings.channels.proof)
            embed = discord.Embed(
                title = "🧶 | Доказательства",
                description = f'''<a:768563657390030971:1041076662546219168>  **Модератор:** <@{interaction.user.id}>\n<a:768563657390030971:1041076662546219168>  **Нарушитель:** <@{нарушитель.id}>\n<a:768563657390030971:1041076662546219168>  **Время наказания:** {время}\n<a:768563657390030971:1041076662546219168>  **Доказательство:** ||{file.url}||''',
                color = 0x98c379,
                timestamp = datetime.datetime.now()
            )
            embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
            embed.set_image(url = file.url)
            await ch.send(embed=embed)
            await interaction.response.send_message('*Доказательства успешно отправлены!*', ephemeral = True)


    @app_commands.command(name = "artmany", description = "Сохраните арты в архив!")
    async def artmany(
            self, interaction: discord.Interaction,
            айди: str,
            айди2: str,
            айди3: str,
            айди4: str,
            айди5: str
    ):
        role = interaction.guild.get_role(1071139216580419644)

        if role not in interaction.user.roles:
            await interaction.response.send_message('*У Вас недостаточно прав! Вам необходимо иметь роль <@&1071139216580419644>*')
            return
        elif role in interaction.user.roles:
            general_art = discord.utils.get(interaction.guild.channels, id=settings.channels.art)
            archive_art = discord.utils.get(interaction.guild.channels, id=settings.channels.archive_art)
            lst = [айди, айди2, айди3, айди4, айди5]
            for id in lst:
                msg = await general_art.fetch_message(int(id))
                attachment = msg.attachments[0]

                embed = discord.Embed(
                    title="",
                    description="",
                    timestamp=msg.created_at,
                    color=msg.author.color
                )
                embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
                embed.set_author(name=f"Арт от {msg.author.display_name}", icon_url=msg.author.avatar.url)
                embed.set_image(url=f"{attachment.url}")
                await archive_art.send(embed=embed)
            await interaction.response.send_message('*Готово!*', ephemeral=True)

    @app_commands.command(name = "emid", description = "Узнайте айди эмодзи!")
    async def emid(
            self, interaction: discord.Interaction,
            эмодзи: str
    ):
        for em in interaction.guild.emojis:
            if em.name == эмодзи: await interaction.response.send_message(f'*<:{em.name}:{em.id}> — {em.id}*', ephemeral = True)



async def setup(client):
    await client.add_cog(adm(client))
