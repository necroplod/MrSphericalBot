import config.config as config
import settings
import asyncio

import datetime
import discord
from discord.ext import commands

class logs(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(" ")
        print(f'----------------------------------------------------')
        print(f"| Logged on as MrSphericalBot - {self.client.user.id} |")
        print(f"| Canary: {config.CANARY}                                    |")
        print(f"| Discord.py Version: {discord.__version__}                        |")
        print(f'----------------------------------------------------')
        print(" ")
        logs = self.client.get_channel(1102889033593536542)
        embed = discord.Embed(
            title = '🎲 | Панель Управления',
            description = f'''
            <a:768563657390030971:1041076662546219168>  **Действие:** Включение бота
            <a:768563657390030971:1041076662546219168>  **Время:** {datetime.datetime.now()}''',
            color = 0xcdc9a5
        )
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await logs.send(embed=embed)

        wilds = self.client.get_channel(settings.channels.wilds)
        await wilds.send('sync', delete_after = 1)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == settings.channels.wilds and message.content == 'sync':
            await self.client.tree.sync()



async def setup(client):
    await client.add_cog(logs(client))