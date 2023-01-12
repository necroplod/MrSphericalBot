import discord
from discord.ext import commands

bans = []

class blacklist(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):


        if member.id not in bans:
            return
        else:
            await member.ban(reason="Многократные нарушения правил, угрозы, превышения полномочий.")
            
            notify = self.client.get_user(678632704874381334)
            embed = discord.Embed(
                title = "🎱 |  Авто-Бан",
                description = f"Пользователь {member} попытался зайти на сервер!",
                color = 0xc01919
            )
            embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} © Created by blackhome7 | Все права защищены')
            await notify.send(embed=embed)


        


def setup(client):
    client.add_cog(blacklist(client))