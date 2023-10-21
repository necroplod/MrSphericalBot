import discord
import settings
from discord.ext import commands


class suggest(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = self.client.get_channel(message.channel.id)

        if message.channel.id in settings.channels.suggest:
            if message.author.bot: return
            else:
                if message.content.startswith('^') or message.content.startswith(':'): return
                else:
                    att = []
                    if message.attachments == []:
                        embed = discord.Embed(
                            title = "",
                            description = f'{message.author.mention} — {message.content}',
                            timestamp = message.created_at,
                            color = 0xfc652c
                        )
                        embed.set_author(name = f"Идея от {message.author.display_name}", icon_url = message.author.avatar.url)
                        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
                    else:
                        for m in message.attachments:
                            f = await m.to_file(filename=f"{m.filename}", use_cached=True)
                            att.append(f)
                        embed = discord.Embed(
                            title = "",
                            description = f'{message.author.mention} — {message.content}',
                            timestamp = message.created_at,
                            color = 0xfc652c
                        )
                        embed.set_author(name = f"Идея от {message.author.display_name}", icon_url = message.author.avatar.url)
                        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
                    await message.delete()
                    msg1 = await channel.send(embed=embed, files = att)
                    if message.channel.id != settings.channels.todo:
                        await msg1.create_thread(name = "🛶 | Обсуждение")
                        await msg1.add_reaction('👍')
                        await msg1.add_reaction('👎')
                    else:
                        await msg1.add_reaction('✔')
                        await msg1.add_reaction('❌')
        else:
            return

async def setup(client):
    await client.add_cog(suggest(client))