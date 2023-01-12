import settings

import datetime
import discord
from discord.ext import commands

class events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(" ")
        print(f'----------------------------------------------------')
        print(f"| Logged on as MrSphericalBot - {self.client.user.id} |")
        print(f"| Discord.py Version: {discord.__version__}                        |")
        print(f'----------------------------------------------------')
        print(" ")    
        await self.client.change_presence(status=discord.Status.online, activity=discord.Streaming(name=f's.help', url='https://www.youtube.com/c/%D0%9C%D0%B8%D1%81%D1%82%D0%B5%D1%80%D0%A1%D1%84%D0%B5%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9'))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
                title = ':warning: | О нет, произошла ошибка в команде!', 
                description = f'**Команда не найдена или введена неправильно!**', 
                color = 0xDB0F0F
            )
            embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
            await ctx.send(embed=embed, delete_after=5)
        if isinstance(error, commands.errors.MissingPermissions):
            embed = discord.Embed(
                title = '🕹 | Недостаточно прав!',
                description = "**У вас не хватает прав для использование этой команды!**",
                color = discord.Color.red()
            )
            embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
            await ctx.send(embed = embed, delete_after=5)
        if isinstance(error, commands.errors.CommandInvokeError):
            embed = discord.Embed(
                title = '🐞 | Ошибка!', 
                description = "**Произошла техническая неполадка в коде, данные об баге были отправлены разработчику.**",
                color=discord.Color.red()
            )
            embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
            await ctx.send(embed = embed, delete_after=5)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            logs = self.client.get_channel(settings.channels.bugs)
            embed = discord.Embed(
                title = "🧿 |  Баг",
                description = f'''**• Время:** {datetime.datetime.now()}
                **• Баг:** ```{error}```
                **• Канал:** <#{ctx.message.channel.id}> - {ctx.message.channel.id}
                **• Автор:** <@{ctx.author.id}> - {ctx.author.id}
                **• Сообщение:** `{ctx.message.content}`
                **• Полное Сообщение:** ```{ctx.message}```''',
                color = 0xdaab39
            )
            embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
            await logs.send(embed=embed)

def setup(client):
    client.add_cog(events(client))