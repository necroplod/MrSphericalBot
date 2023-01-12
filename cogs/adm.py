import settings
import datetime
import discord
import asyncio
import random
import re
from discord.ext import commands
from dislash import InteractionClient, ActionRow, Button, ButtonStyle

class adm(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role(952530469751255043, 952530469751255042)
    async def art(self, ctx):
        embed = discord.Embed(
            title = "🏆 | Архив Артов",
            description = "",
            color = 0x81d8d0
        )
        embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
        row = ActionRow(
            Button(
                style = ButtonStyle.green,
                custom_id = 'start_',
                disabled = True,
                emoji = '♻'
            ),
            Button(
                style = ButtonStyle.blurple,
                custom_id = 'add',
                emoji = '🎯'
            ),
            Button(
                style = ButtonStyle.red,
                custom_id = 'clear_',
                disabled = True,
                emoji = '🗑'
            )
        )
        msg = await ctx.send(embed = embed, components=[row])
        on_click = await msg.wait_for_button_click(timeout = 120)
        ch = self.client.get_channel(ctx.channel.id)
        for _ in range(1):
            if on_click.component.id == 'start':
                archive_art = self.client.get_channel(1006834087031488602)
                general_art = self.client.get_channel(997425650904338453)
                async for art in general_art.history(limit = None):
                    for attachment in art.attachments:  
                        archive_art = self.client.get_channel(1006834087031488602)                     
                        embed = discord.Embed(
                            title = "",
                            description = "",
                            timestamp = art.created_at,
                            color = art.author.color
                        )
                        embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                        embed.set_author(name = f"Арт от {art.author.display_name}", icon_url = art.author.avatar_url)
                        embed.set_image(url = f"{attachment.url}")
                        await archive_art.send(embed=embed)
            if on_click.component.id == 'add':
                archive_arts = self.client.get_channel(1006834087031488602)
                general_art = self.client.get_channel(997425650904338453)
                embed = discord.Embed(
                    title = "🏆 | Архив Артов",
                    description = "*Введите ID сообщения!*",
                    color = 0x1ce091
                )
                embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                await on_click.respond(embed=embed)
                id_msg = await self.client.wait_for('message', check=lambda msg: msg.author == ctx.author)
                msg = await general_art.fetch_message(int(id_msg.content))
                attachment = msg.attachments[0]

                embed = discord.Embed(
                    title = "",
                    description = "",
                    timestamp = msg.created_at,
                    color = msg.author.color
                )
                embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                embed.set_author(name = f"Арт от {msg.author.display_name}", icon_url = msg.author.avatar_url)
                embed.set_image(url = f"{attachment.url}")
                await archive_arts.send(embed=embed)
            if on_click.component.id == 'clear':
                archive_arts = self.client.get_channel(1006834087031488602)
                await archive_arts.purge(limit = None)
                embed = discord.Embed(
                    title = "🏆 | Архив Артов",
                    description = "*Архив успешно очищен!*",
                    color = 0x1ce091
                )
                embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                await ch.send(embed=embed)

    @commands.command()
    @commands.has_any_role(997425461317599272, 952530469751255041, 952530469751255042, 952530469751255043)
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

        logembed = discord.Embed(title="🎉 | Новый Розыгрыш",
                             description=f"**Приз:** ``{msg4.content}``\n**Победителей:** ``{winerscount}``\n**Канал:** {giveawaychannel.mention}\n**Создатель:** {ctx.author.mention}",
                             color=discord.Color.red())
        logembed.set_thumbnail(url=ctx.author.avatar_url)

        logchannel = ctx.guild.get_channel(1011208572895510628)
        await logchannel.send(embed=logembed)

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
                users = await reaction.users().flatten()
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
    @commands.has_any_role(997425461317599272, 952530469751255041, 952530469751255042, 952530469751255043)
    async def reroll(self, ctx):
        async for message in ctx.channel.history(limit=100, oldest_first=False):
            if message.author.id == self.client.user.id and message.embeds:
                reroll = await ctx.fetch_message(message.id)
                users = await reroll.reactions[0].users().flatten()
                users.pop(users.index(self.client.user))
                winner = random.choice(users)
                await ctx.send(f"Новый победитель - это {winner.mention}")
                break
        else:
            await ctx.send("На этом канале не проводится никаких розыгрышей призов.")

    @commands.command()
    @commands.has_any_role(952530469751255043, 952530469751255042)
    async def archive(self, ctx):
        embed = discord.Embed(
            title = "📚 | Архив Каналов",
            description = "",
            color = 0x674ea7
        )
        embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')

        row = ActionRow(
            Button(
                style = ButtonStyle.red,
                custom_id = 'cancel',
                label = 'Отмена',
                emoji = '🔓'
            ),
            Button(
                style = ButtonStyle.blurple,
                custom_id = 'ticket',
                label = 'Тикет',
                emoji = '🎟'
            ),
            Button(
                style = ButtonStyle.blurple,
                custom_id = 'channel',
                label = 'Канал',
                emoji = '📚'
            ),
        )
        msg = await ctx.send(embed = embed, components=[row])
        on_click = await msg.wait_for_button_click(timeout = 120)
        ch = self.client.get_channel(ctx.channel.id)
        for _ in range(1):
            if on_click.component.id == 'cancel':
                embed = discord.Embed(
                    title = "📚 | Архив Каналов",
                    description = "**Действие было отменено пользователем**",
                    color = 0x674ea7
                )
                embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                await msg.edit(embed = embed)
            if on_click.component.id == 'ticket':
                if ctx.channel.name.startswith('closed'):
                    category = discord.utils.get(ctx.guild.channels, name=settings.channels.ticket_archive)
                    embed = discord.Embed(
                        title = "📚 | Архив Каналов",
                        description = "**Перемещение тикета в архив....**",
                        color = 0x674ea7
                    )
                    embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                    await ch.send(embed = embed)
                    await ch.edit(
                        sync_permissions = True,
                        category = category,
                        reason = f'Архивирование канала | {ctx.author.name}#{ctx.author.discriminator}'
                    )
                else:
                    embed = discord.Embed(
                        title = "📚 | Архив Каналов",
                        description = "**Данный тикет не закрыт, перемещение невозможно.**",
                        color = 0x674ea7
                    )
                    embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                    await ch.send(embed = embed)
            if on_click.component.id == 'channel':
                category = discord.utils.get(ctx.guild.channels, name=settings.channels.main_archive)
                embed = discord.Embed(
                    title = "📚 | Архив Каналов",
                    description = "**Перемещение канала в архив....**",
                    color = 0x674ea7
                )
                embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                await ch.send(embed = embed)
                await ch.edit(
                    name = f'{ctx.channel.name}_архив',
                    sync_permissions = True,
                    category = category,
                    reason = f'Архивирование канала | {ctx.author.name}#{ctx.author.discriminator}'
                )

def setup(client):
    client.add_cog(adm(client))
