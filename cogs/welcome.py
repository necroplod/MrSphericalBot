import discord
from discord.ext import commands

class welcome(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome = self.client.get_channel(952530469751255049)
        rules = f"<#959770387204415498>"
        verify = f"<#959752658313437274>"
#        navigation = f"<#959774875642372096>"
#        embed = discord.Embed(title=' ', color=0x2ecc71, description=f'''{member.mention}, Добро Пожаловать на сервер **Мистер Сферический**!
#
#        Вот тебе каналы для ознакомления: {rules}, {navigation}, но перед этим пройди верификацию в {verify}!''')

        embed = discord.Embed(title=' ', color=0x2ecc71, description=f'''{member.mention}, Добро Пожаловать на сервер **Мистер Сферический**!
        
        Не забудь прочитать {rules} и пройти верификацию в {verify}!''')
        embed.set_image(url="https://cdn.discordapp.com/attachments/959385309374713896/977190213816287313/unknown.png?size=4096")
        await welcome.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        welcome = self.client.get_channel(952530469751255049)
        embed = discord.Embed(title=' ', color=0x2ecc71, description=f'**{member}** Покинул наш сервер :(')
        embed.set_image(url="https://cdn.discordapp.com/attachments/959385309374713896/977190225862361099/unknown.jpeg?size=4096")
        await welcome.send(embed=embed)






def setup(client):
    client.add_cog(welcome(client))