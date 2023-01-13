import discord
from discord.ext import commands

prefix = 's.'

class info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
      embed = discord.Embed(title = '📚 | Доступные Команды:', description = ' ', colour = discord.Color.red())

      embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar.url)
      embed.add_field(name = '<:khrushchev:1005361978442780680>  Информация', value = f'`{prefix}help`', inline=False)
      embed.add_field(name = '<:earch:1005361448513445888>  Веселье', value = f'`{prefix}catkdk` `{prefix}kdk` `{prefix}kdkeat`', inline=False)
      embed.add_field(name = '<:king:1005355877278154814>  Админские Штучки', value = f'`{prefix}giveaway` `{prefix}reroll` `{prefix}art` `{prefix}archive`', inline=False)
      embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
      await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(info(client))