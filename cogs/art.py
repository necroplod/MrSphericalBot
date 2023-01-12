import discord
from discord.ext import commands
from dislash import InteractionClient, ActionRow, Button, ButtonStyle

class art(commands.Cog):

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
        embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} © Created by blackhome7 | Все права защищены')
        row = ActionRow(
            Button(
                style = ButtonStyle.green,
                custom_id = 'start',
                emoji = '♻'
            ),
            Button(
                style = ButtonStyle.blurple,
                custom_id = 'add',
                emoji = '🎯'
            ),
            Button(
                style = ButtonStyle.red,
                custom_id = 'clear',
                emoji = '🗑'
            )
        )
        msg = await ctx.send(embed = embed, components=[row])
        on_click = await msg.wait_for_button_click(timeout = 120)
        ch = self.client.get_channel(ctx.channel.id)
        for _ in range(1):
            if on_click.component.id == 'start':
                archive_art = self.client.get_channel(1006834087031488602)
                test = self.client.get_channel(997425610207006800)
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
                        embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} © Created by blackhome7')
                        embed.set_author(name = f"Арт от {art.author.display_name}", icon_url = art.author.avatar_url)
                        embed.set_image(url = f"{attachment.url}")
                        await archive_arts.send(embed=embed)
            if on_click.component.id == 'add':
                archive_arts = self.client.get_channel(1006834087031488602)
                general_art = self.client.get_channel(997425650904338453)
                embed = discord.Embed(
                    title = "🏆 | Архив Артов",
                    description = "*Введите ID сообщения!*",
                    color = 0x1ce091
                )
                embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} © Created by blackhome7 | Все права защищены')
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
                embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} © Created by blackhome7')
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
                embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} © Created by blackhome7 | Все права защищены')
                await ch.send(embed=embed)













def setup(client):
    client.add_cog(art(client))
