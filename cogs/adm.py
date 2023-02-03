import settings
import datetime
import discord
import asyncio
import random
import re
from discord.ext import commands
from discord.ui.view import View
from discord.ui.modal import Modal


class Art_id(Modal, title = '🎇 | ID'):
    msg = discord.ui.TextInput(
        label = 'ID сообщения',
    )
    async def on_submit(self, interaction: discord.Interaction):
        general_art = discord.utils.get(interaction.guild.channels, name=settings.channels.art)
        archive_art = discord.utils.get(interaction.guild.channels, name=settings.channels.archive_art)
        msg = await general_art.fetch_message(int(self.msg.value))
        attachment = msg.attachments[0]

        embed = discord.Embed(
            title = "",
            description = "",
            timestamp = msg.created_at,
            color = msg.author.color
        )
        embed.set_author(name = f"Арт от {msg.author.display_name}", icon_url = msg.author.avatar.url)
        embed.set_image(url = f"{attachment.url}")
        await archive_art.send(embed=embed)
class Art(discord.ui.View):
        def __init__(self, *, timeout=180):
            super().__init__(timeout=timeout)
            
        @discord.ui.button(emoji = '♻', style = discord.ButtonStyle.green, disabled = True)
        async def start(self, interaction: discord.Interaction, button: discord.ui.Button):
            archive_art = discord.utils.get(interaction.guild.channels, name=settings.channels.archive_art)
            general_art = discord.utils.get(interaction.guild.channels, name=settings.channels.art)
            async for art in general_art.history(limit = None):
                for attachment in art.attachments:            
                    embed = discord.Embed(
                        title = "",
                        description = "",
                        timestamp = art.created_at,
                        color = art.author.color
                    )
                    embed.set_author(name = f"Арт от {art.author.display_name}", icon_url = art.author.avatar.url)
                    embed.set_image(url = f"{attachment.url}")
                    await archive_art.send(embed=embed)
        @discord.ui.button(emoji = '🎯', style = discord.ButtonStyle.blurple)
        async def add(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_modal(Art_id())

        @discord.ui.button(emoji = '🗑', style = discord.ButtonStyle.blurple, disabled = True)
        async def clear(self, interaction: discord.Interaction, button: discord.ui.Button):
            archive_art = discord.utils.get(interaction.guild.channels, name=settings.channels.archive_art)
            await archive_art.purge(limit = None)
            embed = discord.Embed(
                title = "🏆 | Архив Артов",
                description = "*Архив успешно очищен!*",
                color = 0x1ce091
            )
            embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
            await interaction.response.edit_message(self=view, embed=embed)
class Archive(discord.ui.View):
        def __init__(self):
            super().__init__()
            
        @discord.ui.button(emoji = '🔓', style = discord.ButtonStyle.red, label = 'Отмена')
        async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
            embed = discord.Embed(
                title = "📚 | Архив Каналов",
                description = "<a:768563657390030971:1041076662546219168> **Действие было отменено пользователем**",
                color = 0x674ea7
            )
            embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
            await interaction.response.edit_message(view=None, embed=embed)
        @discord.ui.button(emoji = '🎟', style = discord.ButtonStyle.blurple, label = 'Тикет')
        async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
            category = discord.utils.get(interaction.guild.channels, name=settings.channels.ticket_archive)
            if len(category.channels) > 48:
                embed = discord.Embed(
                    title="📚 | Архив Каналов",
                    description="<a:768563657390030971:1041076662546219168> **Архив засорился!**",
                    color=0x674ea7
                )
                embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
                embed.set_image(url="https://media.tenor.com/r3t0LfS0dCwAAAAd/toilet-meme.gif")
                await interaction.response.edit_message(view=None, embed=embed)
            else:
                embed = discord.Embed(
                    title = "📚 | Архив Каналов",
                    description = "<a:768563657390030971:1041076662546219168> **Перемещение тикета в архив....**",
                    color = 0x674ea7
                )
                embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
                await interaction.response.edit_message(view=None, embed=embed)
                ch = interaction.channel
                await ch.edit(
                    sync_permissions = True,
                    category = category,
                    reason = f'Архивирование канала | {interaction.user.name}#{interaction.user.discriminator}'
                )
        @discord.ui.button(emoji = '📚', style = discord.ButtonStyle.blurple, label = 'Канал')
        async def channel(self, interaction: discord.Interaction, button: discord.ui.Button):
            category = discord.utils.get(interaction.guild.channels, name=settings.channels.main_archive)
            embed = discord.Embed(
                title = "📚 | Архив Каналов",
                description = "<a:768563657390030971:1041076662546219168> **Перемещение канала в архив....**",
                color = 0x674ea7
            )
            embed.set_footer(icon_url = settings.misc.avatar_url, text = settings.misc.footer)
            await interaction.response.edit_message(view=None, embed=embed)
            ch = interaction.channel
            await ch.edit(
                name = f'{interaction.channel.name}_архив',
                sync_permissions = True,
                category = category,
                reason = f'Архивирование канала | {interaction.user.name}#{interaction.user.discriminator}'
            )
class Poll_modal(Modal, title = '🎁 | Опрос'):
    ch = discord.ui.TextInput(label = "ID Канала:", placeholder = "Оставьте пустым, если опрос будет в этом канале", required = False)
    name = discord.ui.TextInput(label = "Тема опроса:", required = True)
    option_1 = discord.ui.TextInput(label = "Первый вариант ответа:", required = True)
    option_2 = discord.ui.TextInput(label = "Второй вариант ответа:", required = True)
    option_3 = discord.ui.TextInput(label = "Третий вариант ответа:", placeholder = "Этот вариант можно оставить пустым",required = False)

    async def on_submit(self, interaction: discord.Interaction):
        one = f":one: {self.option_1.value}"
        two = f":two: {self.option_2.value}"
        if self.option_3.value == '':
            three = ''
        else:
            three = f":three: {self.option_3.value}"


        embed = discord.Embed(
            title = '🎁 | Опрос',
            description = f"""
**{self.name.value}**
{one}
{two}
{three}""",
            color = 0x007f5c
        )
        embed.set_footer(icon_url=settings.misc.avatar_url, text=settings.misc.footer)
        embed.set_author(name = interaction.user.display_name, icon_url= interaction.user.display_avatar)

        if self.ch.value == '':
            msg = await interaction.channel.send(f'<@&{settings.misc.poll_role}>', embed=embed)
        else:
            channel = discord.utils.get(interaction.guild.channels, id = int(self.ch.value))
            msg = await channel.send(f'<@&{settings.misc.poll_role}>', embed=embed)
        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        if self.option_3.value != '':
            await msg.add_reaction('3️⃣')



class Poll(View):
    def __init__(self, *, timeout=60):
        super().__init__(timeout=timeout)

    @discord.ui.button(emoji='🎋', style=discord.ButtonStyle.green, label = 'Создать опрос')
    async def poll(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(Poll_modal())
class adm(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role(1071139216580419644)
    async def art(self, ctx):
        embed = discord.Embed(
            title = "🏆 | Архив Артов",
            description = "",
            color = 0x81d8d0
        )
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        msg = await ctx.send(embed = embed, view = Art())

    @commands.command()
    @commands.has_any_role(1071139413586882652)
    async def giveaway(self, ctx):
        await ctx.send("Выберите канал, на котором вы хотели бы провести розыгрыш призов.")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            msg1 = await self.client.wait_for('message', check=check, timeout=30.0)

            channel_converter = discord.ext.commands.TextChannelConverter()
            try:
                giveawaychannel = await channel_converter.convert(ctx, msg1.content)
            except commands.BadArgument:
                return await ctx.send("Этот канал не существует, пожалуйста, попробуйте еще раз.")

        except asyncio.TimeoutError:
            await ctx.send("Вы слишком долго ждали, пожалуйста, попробуйте еще раз!")

        if not giveawaychannel.permissions_for(ctx.guild.me).send_messages or not giveawaychannel.permissions_for(
                ctx.guild.me).add_reactions:
            return await ctx.send(
                f"У бота нет правильных разрешений для отправки: {giveawaychannel}\n ** Необходимые разрешения: ** ``Добавлять реакции | Отправлять сообщения``.")

        await ctx.send("Сколько победителей розыгрыша вы бы хотели?")
        try:
            msg2 = await self.client.wait_for('message', check=check, timeout=30.0)
            try:
                winerscount = int(msg2.content)
            except ValueError:
                return await ctx.send("Вы не указали количество победителей, пожалуйста, попробуйте еще раз.")

        except asyncio.TimeoutError:
            await ctx.send("Вы слишком долго ждали, пожалуйста, попробуйте еще раз!")

        await ctx.send("Выберите количество времени для розыгрыша призов.")
        try:
            since = await self.client.wait_for('message', check=check, timeout=30.0)

        except asyncio.TimeoutError:
            await ctx.send("Вы слишком долго ждали, пожалуйста, попробуйте еще раз!")

        seconds = ("s", "sec", "secs", 'second', "seconds")
        minutes = ("m", "min", "mins", "minute", "minutes")
        hours = ("h", "hour", "hours")
        days = ("d", "day", "days")
        weeks = ("w", "week", "weeks")
        rawsince = since.content

        try:
            temp = re.compile("([0-9]+)([a-zA-Z]+)")
            if not temp.match(since.content):
                return await ctx.send("Вы не указали единицу времени, пожалуйста, повторите попытку.")
            res = temp.match(since.content).groups()
            time = int(res[0])
            since = res[1]

        except ValueError:
            return await ctx.send("Вы не указали единицу времени, пожалуйста, повторите попытку.")

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
            return await ctx.send("Вы не указали единицу времени, пожалуйста, повторите попытку.")

        await ctx.send("Какой бы вы хотели приз?")
        try:
            msg4 = await self.client.wait_for('message', check=check, timeout=30.0)

        except asyncio.TimeoutError:
            await ctx.send("Вы слишком долго ждали, пожалуйста, попробуйте еще раз.")

        futuredate = datetime.datetime.utcnow() + datetime.timedelta(seconds=timewait)
        embed1 = discord.Embed(color=discord.Color(random.randint(0x000000, 0xFFFFFF)),
                           title=f"🎉 | РОЗЫГРЫШ\n`{msg4.content}`", timestamp=futuredate,
                           description=f'Нажмите на 🎉 чтобы вступить!\nСоздан: {ctx.author.mention}')

        embed1.set_footer(text=f"Розыгрыш закончится")
        msg = await giveawaychannel.send(embed=embed1)
        await msg.add_reaction("🎉")
        await asyncio.sleep(timewait)
        message = await giveawaychannel.fetch_message(msg.id)
        for reaction in message.reactions:
            if str(reaction.emoji) == "🎉":
                users = [user async for user in reaction.users()]
                if len(users) == 1:
                    return await msg.edit(embed=discord.Embed(title="Никто не выиграл в розыгрыше."))
        try:
            winners = random.sample([user for user in users if not user.bot], k=winerscount)
        except ValueError:
            return await giveawaychannel.send("Недостаточно участников")
        winnerstosend = "\n".join([winner.mention for winner in winners])

        win = await msg.edit(embed=discord.Embed(title="🎉 | ПОБЕДИТЕЛЬ",
                                             description=f"Поздравляем {winnerstosend}, вы выиграли **{msg4.content}**!",
                                             color=discord.Color.blue()))

    @commands.command()
    @commands.has_any_role(1071139413586882652)
    async def reroll(self, ctx):
        async for message in ctx.channel.history(limit=100, oldest_first=False):
            if message.author.id == self.client.user.id and message.embeds:
                reroll = await ctx.fetch_message(message.id)
                users = [user async for user in reroll.reactions[0].users()]
                users.pop(users.index(self.client.user))
                winner = random.choice(users)
                await ctx.send(f"Новый победитель - это {winner.mention}")
                break
        else:
            await ctx.send("На этом канале не проводится никаких розыгрышей призов.")           

    @commands.command()
    @commands.has_any_role(1071139692914946109)
    async def archive(self, ctx):
        embed = discord.Embed(
            title = "📚 | Архив Каналов",
            description = "",
            color = 0x674ea7
        )
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        msg = await ctx.send(embed = embed, view = Archive())

    @commands.command()
    @commands.has_any_role(1071139871105744977)
    async def poll(self, ctx):
        embed = discord.Embed(
            title = "🎁 | Опрос",
            description = "",
            color = 0x007f5c
        )
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        author = ctx.author
        await ctx.send(embed = embed, view = Poll())

async def setup(client):
    await client.add_cog(adm(client))
