import discord
import time
import settings
from discord.ext import commands


class suggest(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = self.client.get_channel(message.channel.id)

        if message.channel.id in settings.channels.suggest:
            if message.author.bot:
                return
            else:
                if message.content.startswith('^'):
                    return
                else:
                    embed = discord.Embed(
                        title = "",
                        description = f'{message.author.mention} — {message.content}',
                        timestamp = message.created_at,
                        color = 0xfc652c
                    )
                    embed.set_author(name = f"Идея от {message.author.display_name}", icon_url = message.author.avatar_url)
                    embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                    await message.delete()
                    msg1 = await channel.send(embed=embed)
                    if message.channel.id != settings.channels.todo:
                        await msg1.add_reaction('👍')
                        await msg1.add_reaction('👎')
                    else:
                        await msg1.add_reaction('✔')
                        await msg1.add_reaction('❌')
        else:
            return

def setup(client):
    client.add_cog(suggest(client))