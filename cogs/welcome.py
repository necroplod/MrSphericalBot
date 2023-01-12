import discord
from discord.ext import commands

class welcome(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome = self.client.get_channel(997425613830897674)
        rules = f"<#959770387204415498>"
        verify = f"<#997425580607819840>"
#        navigation = f"<#959774875642372096>"
#        embed = discord.Embed(title=' ', color=0x2ecc71, description=f'''{member.mention}, Добро Пожаловать на сервер **Мистер Сферический**!
#
#        Вот тебе каналы для ознакомления: {rules}, {navigation}, но перед этим пройди верификацию в {verify}!''')

        embed = discord.Embed(title=' ', color=0x2ecc71, description=f'''{member.mention}, Добро Пожаловать на сервер **Мистер Сферический**!
        
        Не забудь прочитать {rules} и пройти верификацию в {verify}!''')
        embed.set_image(url="https://i.ytimg.com/vi/nVzqh0fTARU/hqdefault.jpg")
        embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} © Created by blackhome7 | Все права защищены')
        await welcome.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        welcome = self.client.get_channel(997425613830897674)
        embed = discord.Embed(title=' ', color=0x2ecc71, description=f'**{member}** Покинул наш сервер :(')
        embed.set_image(url="https://i.ytimg.com/vi/F_e2eknfMbU/hqdefault.jpg")
        embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} © Created by blackhome7 | Все права защищены')
        await welcome.send(embed=embed)






def setup(client):
    client.add_cog(welcome(client))