import settings

import discord
from discord.ext import commands

class rp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def msg(self, ctx):
        if ctx.guild.id != settings.misc.guild_rp:
            embed = discord.Embed(
                title = "🎪 | ВПИ",
                description = "<a:768563657390030971:1041076662546219168> **Данная команда доступна только на ВПИ сервере!**",
                color = 0x003366
            )
            embed.set_footer(icon_url=self.client.user.avatar.url, text=f'{self.client.user.name} | Все права защищены')
            await ctx.send(embed=embed)
        elif ctx.guild.id == settings.misc.guild_rp:
            role = discord.utils.get(ctx.guild.roles, id=1069695539257557053)
            if role in ctx.author.roles:
                await ctx.send('От чьего имени будет сообщение?')
                name = await self.client.wait_for('message', check=lambda msg: msg.author == ctx.author)
                name = name.content

                await ctx.send('Отправьте аватарку.')
                icon = await self.client.wait_for('message', check=lambda msg: msg.author == ctx.author)
                icon = icon.attachments[0]

                await ctx.send('Какой текст будет?')
                txt = await self.client.wait_for('message', check=lambda msg: msg.author == ctx.author)
                txt = txt.content

                await ctx.send('В какой канал будет отправлено сообщение(ID Канала)? (Напишите none, если хотите в этот)')
                location = await self.client.wait_for('message', check=lambda msg: msg.author == ctx.author)
                location = location.content
                if location != 'none':
                    ch = int(location)
                elif location == 'none':
                    ch = ctx.channel.id
                chn = self.client.get_channel(ch)
                embed = discord.Embed(
                    description = f"*{txt}*",
                    color = 0x003366,
                )
                embed.set_author(name=name, icon_url=icon.url)
                embed.set_footer(icon_url=self.client.user.avatar.url, text=f'{self.client.user.name} | Все права защищены')

                await chn.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="🎪 | ВПИ",
                    description="<a:768563657390030971:1041076662546219168> **У Вас отсутствует роль <@&1069695539257557053>!**",
                    color=0x003366
                )
                embed.set_footer(icon_url=self.client.user.avatar.url,
                                 text=f'{self.client.user.name} | Все права защищены')
                await ctx.send(embed=embed)

    


async def setup(client):
    await client.add_cog(rp(client))