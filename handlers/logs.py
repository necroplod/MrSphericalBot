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
        print(f"| Discord.py Version: {discord.__version__}                       |")
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

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        msg = self.client.get_channel(settings.logs.msg)

        if before.author.bot:
            return
        embed = discord.Embed(
            description=f"*[Сообщение]({before.jump_url}) было отредактировано*\n\n***Старое содержимое:***```{before.content}```***Новое содержимое:***```{after.content}```\n",
            color=0xa77fb3,
            timestamp=datetime.datetime.now()
        )
        embed.add_field(name='Автор:', value=f'*{before.author.name}* (<@{before.author.id}>)', inline=True)
        embed.add_field(name='Канал:', value=f'*{before.channel.name}* (<#{before.channel.id}>)', inline=True)
        embed.add_field(name='Айди:', value=f'*{before.id}* ({before.jump_url})', inline=True)
        embed.set_footer(icon_url=self.client.user.avatar.url, text=f'{self.client.user.name} | Все права защищены')
        await msg.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        msg = self.client.get_channel(settings.logs.msg)

        if message.author.bot:
            return
        if message.attachments:
            lst = []
            for m in message.attachments:
                f = await m.to_file(filename=f"{m.filename}", use_cached=True)
                lst.append(f)

            embed = discord.Embed(
                description=f"*Сообщение было удалено*\n\n",
                color=0xa77fb3,
                timestamp=datetime.datetime.now()
            )
            embed.add_field(name='Автор:', value=f'*{message.author.name}* (<@{message.author.id}>)', inline=True)
            embed.add_field(name='Канал:', value=f'*{message.channel.name}* (<#{message.channel.id}>)', inline=True)
            embed.set_footer(icon_url=self.client.user.avatar.url, text=f'{self.client.user.name} | Все права защищены')
            await msg.send(embed=embed, files = lst)
        if not message.attachments:
            embed = discord.Embed(
                description=f"*Сообщение было удалено*\n\n***Cодержимое:***```{message.content}```\n",
                color=0xa77fb3,
                timestamp=datetime.datetime.now()
            )
            embed.add_field(name='Автор:', value=f'*{message.author.name}* (<@{message.author.id}>)', inline=True)
            embed.add_field(name='Канал:', value=f'*{message.channel.name}* (<#{message.channel.id}>)', inline=True)
            embed.set_footer(icon_url=self.client.user.avatar.url, text=f'{self.client.user.name} | Все права защищены')
            await msg.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        role = self.client.get_channel(settings.logs.role)
        bef = [r.mention for r in before.roles]
        aft = [r.mention for r in after.roles]
        if before.roles != after.roles:
            embed = discord.Embed(
                description=f"*Роли участника были изменены*\n",
                color=0xd0d3d5,
                timestamp=datetime.datetime.now()
            )
            embed.set_footer(icon_url=self.client.user.avatar.url, text=f'{self.client.user.name} | Все права защищены')
            embed.add_field(name = 'Участник:', value = f'*{before.name}* (<@{before.id}>)', inline=True)
            embed.add_field(name = 'Роли до:', value = "\n".join(bef), inline=True)
            embed.add_field(name = 'Роли после:', value = "\n".join(aft), inline=True)
            await role.send(embed=embed)
            
    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome = self.client.get_channel(settings.logs.welcome)
        embed = discord.Embed(
            description = f"*Участник **{member.name}**(<@{member.id}>) присоединился к серверу*",
            color=0x35a661,
            timestamp=datetime.datetime.now()
        )
        embed.set_thumbnail(url = member.avatar.url)
        embed.add_field(name = "Дата регистрации:", value = f"*{member.created_at.strftime('%d.%m.%Y')}*")
        embed.set_footer(icon_url=self.client.user.avatar.url, text=f'{self.client.user.name} | Все права защищены')
        await welcome.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        welcome = self.client.get_channel(settings.logs.welcome)
        r = [r.mention for r in member.roles]
        embed = discord.Embed(
            description = f"*Участник **{member.name}**(<@{member.id}>) покинул сервер*",
            color=0xa60530,
            timestamp=datetime.datetime.now()
        )
        embed.set_thumbnail(url = member.avatar.url)
        embed.add_field(name = "Дата регистрации:", value = f"*{member.created_at.strftime('%d.%m.%Y')}*")
        embed.add_field(name = "Дата захода:", value=f"*{member.joined_at.strftime('%d.%m.%Y')}*")
        embed.add_field(name = 'Роли:', value = "\n".join(r), inline=True)
        embed.set_footer(icon_url=self.client.user.avatar.url, text=f'{self.client.user.name} | Все права защищены')
        await welcome.send(embed=embed)



async def setup(client):
    await client.add_cog(logs(client))