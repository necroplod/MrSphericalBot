import discord
from discord.ext import commands

bans = [
       972546611685261312, # atom bot
       962808419998388234, # Сфер-помощник
       663067667170721802, # StLukas
       397340943570698240, # Спамтон.Г.Спамтон
       932509836787187764, # Точно не твинк севы
       932490997194166344, # samiysok
       932598202719404042, # stepback
       977845936996896838, # kykikekikeks
       954046288104685568, # sevaatom
       489082344159051786, # atomseva
       932611419197816832, # Военкомат
       933030522186264596, # BigSmoke
       932541542219006013, # Walter_FS
       821762235243954216, # kjkszpj
       858376307321733130, # valik505🇾🇪
       781859323831123970  # сасил
       ]

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