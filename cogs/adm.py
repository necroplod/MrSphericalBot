import typing

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

class RecruitModal(discord.ui.Modal, title = '🏆 | Заявка'):
    post = discord.ui.TextInput(label = "Должность", placeholder = "Актив менеджер, модератор и т.д.", required = True)
    nameage = discord.ui.TextInput(label = "Имя, возраст", placeholder = "Иван, 16 лет...", required=True)
    skill = discord.ui.TextInput(label = "Особые навыки", required=True)
    time = discord.ui.TextInput(label = "Сколько готовы уделять серверу?", placeholder = "3-5 часов", required=True)
    why = discord.ui.TextInput(label = "Почему мы должны взять именно Вас?", required = True)

    async def on_submit(self, interaction: discord.Interaction):
        ch = interaction.guild.get_channel(settings.channels.recruit)
        user = interaction.user

        if (datetime.datetime.now(datetime.timezone.utc) - user.created_at) < datetime.timedelta(days = 31):
            await interaction.response.send_message('*Вы зарегистрированы в дискорде меньше месяца!*', ephemeral = True)
            return
        if (datetime.datetime.now(datetime.timezone.utc) - user.joined_at) < datetime.timedelta(days = 7):
            await interaction.response.send_message('*Вы зашли на сервер меньше недели назад!*', ephemeral=True)
            return
        else:
            embed = discord.Embed(title = "🏆 | Заявка", color = 0xcfb53b)
            embed.add_field(name = "Основное:", value = f"<:sunsmirk:1008138014410674299>  Участник <@{user.id}>\n<:Poslkastrong:1062849475808350238>  Айди: {user.id}\n<:Vo:1079126733095174296>  Дата регистрации: <t:{round(user.created_at.timestamp())}:D> (<t:{round(user.created_at.timestamp())}:R>)", inline = False)
            embed.add_field(name = "Сервер:", value = f"<:Switzerland:1047955071612244059>  Дата захода: <t:{round(user.joined_at.timestamp())}:D> (<t:{round(user.joined_at.timestamp())}:R>)\n<:krutoi:1071734769395716116>  Высшая роль: <@&{user.top_role.id}>", inline = False)
            embed.add_field(name = "<:Nasaniash:1063562901958438922>  Заявка:", value = f"— {self.post.value}\n— {self.nameage.value}\n— {self.skill.value}\n— {self.time.value}\n— {self.why.value}", inline = False)
            embed.set_thumbnail(url = interaction.user.avatar.url)
            embed.set_footer(icon_url = settings.misc.avatar_url, text = settings.misc.footer)

            await ch.send(embed=embed)
            await interaction.response.send_message('*Отправлено!*', ephemeral = True)

class RecruitView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(emoji='🎲', style=discord.ButtonStyle.green, label = 'Отправить заявку', custom_id = "recruit_view:create")
    async def create(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(RecruitModal())
    @discord.ui.button(emoji='🎯', style=discord.ButtonStyle.red, label='Закрыть набор',custom_id="recruit_view:close")
    async def close(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user
        if user.guild_permissions.administrator:
            embed = discord.Embed(
                title = "🏆 | Заявка",
                description = f">>> *Набор в персонал был закрыт администратором <@{user.id}>.\nВсем спасибо за участие, быть может повезет в следующий раз...*",
                color = 0x9c3f3f
            )
            embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
            await interaction.response.edit_message(embed=embed, view = None)
        else:
            await interaction.response.send_message('*У Вас недостаточно прав! Вам необходимо иметь права администратора!*', ephemeral=True)

class adm(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == settings.channels.art and message.attachments:
            if "^" in message.content:
                pass
            else:
                await message.create_thread(name = "🛶 | Обсуждение")
                await message.add_reaction("🤍")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        general_art = reaction.message.guild.get_channel(settings.channels.art)
        archive_art = reaction.message.guild.get_channel(settings.channels.archive_art)
        role = reaction.message.guild.get_role(1071139216580419644)

        if reaction.emoji == "🤍" and role in user.roles:
            msg = await general_art.fetch_message(int(reaction.message.id))
            attachment = msg.attachments[0]

            embed = discord.Embed(
                title="",
                description=f"{msg.jump_url}",
                timestamp=msg.created_at,
                color=msg.author.color
            )
            embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
            if msg.author.avatar.url is None:
                embed.set_author(name=f"Арт от {msg.author.display_name}", icon_url=settings.misc.avatar_url)
            else:
                embed.set_author(name=f"Арт от {msg.author.display_name}", icon_url=msg.author.avatar.url)
            embed.set_image(url=f"{attachment.url}")
            await archive_art.send(embed=embed)

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
                description=f"{msg.jump_url}",
                timestamp=msg.created_at,
                color=msg.author.color
            )
            embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
            if msg.author.avatar.url is None:
                embed.set_author(name=f"Арт от {msg.author.display_name}", icon_url=settings.misc.avatar_url)
            else:
                embed.set_author(name=f"Арт от {msg.author.display_name}", icon_url=msg.author.avatar.url)
            embed.set_image(url=f"{attachment.url}")
            await archive_art.send(embed=embed)
            await interaction.response.send_message('*Готово!*', ephemeral=True)

    @app_commands.command(name = "poll", description = "Создайте опрос")
    async def poll(
            self, interaction: discord.Interaction,
            тема: str,
            канал: Union[discord.TextChannel],
            вариант1: str,
            вариант2: str,
            вариант3: str,
            вариант4: str,
            роль: Union[discord.Role]

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
            role = роль.id


            embed = discord.Embed(
                title='🎁 | Опрос',
                description=f"""**{тема}**\n{one}\n{two}\n{three}\n{four}
            """,
                color=0x007f5c
            )
            embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
            embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar)

            msg = await канал.send(f'<@&{role}>', embed=embed)

            await msg.add_reaction('1️⃣')
            await msg.add_reaction('2️⃣')
            await msg.add_reaction('3️⃣')
            await msg.add_reaction('4️⃣')


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
            file_ = await file.to_file(filename=f"{file.filename}", use_cached=True)
            embed = discord.Embed(
                title = "🧶 | Доказательства",
                description = f'''<a:768563657390030971:1041076662546219168>  **Модератор:** <@{interaction.user.id}>\n<a:768563657390030971:1041076662546219168>  **Нарушитель:** <@{нарушитель.id}>\n<a:768563657390030971:1041076662546219168>  **Время наказания:** {время}''',
                color = 0x98c379,
                timestamp = datetime.datetime.now()
            )
            embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
            await ch.send(embed=embed)
            await ch.send(file = file_)
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
            if айди2 == "0": lst.remove(айди2)
            if айди3 == "0": lst.remove(айди3)
            if айди4 == "0": lst.remove(айди4)
            if айди5 == "0": lst.remove(айди5)
            for id in lst:
                msg = await general_art.fetch_message(int(id))
                attachment = msg.attachments[0]

                embed = discord.Embed(
                    title="",
                    description=f"{msg.jump_url}",
                    timestamp=msg.created_at,
                    color=msg.author.color
                )
                embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
                if msg.author.avatar.url is None: embed.set_author(name=f"Арт от {msg.author.display_name}", icon_url=settings.misc.avatar_url)
                else: embed.set_author(name=f"Арт от {msg.author.display_name}", icon_url=msg.author.avatar.url)
                embed.set_image(url=f"{attachment.url}")
                await archive_art.send(embed=embed)
            await interaction.response.send_message('*Готово!*', ephemeral=True)


    @app_commands.command(name = "recruit", description = "Создание набора в персонал")
    async def recruit(
            self, interaction: discord.Interaction,
    ):
        user = interaction.user
        if user.guild_permissions.administrator:
            embed = discord.Embed(
                title = "🏆 | Заявка",
                description = f">>> *Для того, чтобы попасть в нашу дружную команду необходимо обладать такими качествами:*\n— адекватность, \n— умение работать в команде, \n— знания русского языка, \n— наличие 2FA, \n— уровень <@310848622642069504> не ниже 10, \n— не меньше месяца аккаунту, \n— не меньше недели на сервере,  \n— ну и самое главное - желание двигаться по карьерной лестнице !",
                color = 0x9c3f3f
            )
            embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
            embed2 = discord.Embed(
                title = "",
                description = '***ВНИМАНИЕ УЧАСТНИКАМ!!!***\n>>> 1. За "рофельные", т.е. шуточные заявки будет выдан пред на 2 недели. При повторе - мут на 6ч. Мы ищем нормальных людей, которые хотят помочь развитию сервера, а не несерьезных приколистов.\n2. Как вы должны знать, для пользования Дискордом вам должно быть от 13 лет включительно. Если будет замечено, что вам меньше 13 лет, вы будете забанены на сервере за нарушение TOS Discord.',
                color = 0xd5f1f6
            )
            embed2.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
            await interaction.response.send_message(embeds=[embed, embed2], view = RecruitView())
        else:
            await interaction.response.send_message('*У Вас недостаточно прав! Вам необходимо иметь права администратора!*', ephemeral=True)




async def setup(client):
    await client.add_cog(adm(client))
