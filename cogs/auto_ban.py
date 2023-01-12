import discord
import asyncio
from discord.ext import commands

bans = [000000000000000000000]

class auto_ban(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_member_join(self, member):

        print(f'{member} - {member.id} Join')

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
            await notify.send(embed=embed)


        


def setup(client):
    client.add_cog(auto_ban(client))