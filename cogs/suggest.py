import discord
import time
from discord.ext import commands

suggest_ch = [
          952610624595177502, # 💎・предложения
          991074855577350184 # ✅・предложения
          ]

class suggest(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = self.client.get_channel(message.channel.id)

        if message.channel.id in suggest_ch:
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
                    await message.delete()
                    msg1 = await channel.send(embed=embed)

                    await msg1.add_reaction('👍')
                    await msg1.add_reaction('👎') 

        else:
            return

def setup(client):
    client.add_cog(suggest(client))