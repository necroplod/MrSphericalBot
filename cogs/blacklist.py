import settings

import discord
from discord.ext import commands
from dislash import ActionRow, Button, ButtonStyle

class blacklist(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.id not in settings.blacklist.bans:
            return
        elif member.id in settings.blacklist.bans:
            await member.ban(reason='Многократные нарушения правил, угрозы, превышения полномочий.')          
            notify = self.client.get_channel(settings.channels.autoban)
            embed = discord.Embed(
                title = "🎱 |  Авто-Бан",
                description = f"Пользователь `{member.name}#{member.discriminator} | {member.id}` попытался зайти на сервер!",
                color = 0xc01919
            )
            embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
            await notify.send(embed=embed)
    """
    @commands.command()
    async def blacklist(self, ctx):       
        if ctx.message.author.id not in config['adm']:
            embed = discord.Embed(
                title = "🎱 |  Авто-Бан",
                description = f"**У вас нет доступа к черному списку!**",
                color = 0xc01919
            )
            embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
            await ctx.send(embed=embed)
        elif ctx.message.author.id in config['adm']:        
            embed = discord.Embed(
                title = "🎱 |  Авто-Бан",
                description = f"",
                color = 0xc01919
            )
            embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
            
            power = ActionRow(
                Button(
                    style = ButtonStyle.green,
                    custom_id = 'on',
                    label = 'Включить',
                    emoji = '✔'
                ),
                Button(
                    style = ButtonStyle.blurple,
                    custom_id = 'disabled',
                    label = '—',
                    disabled = True
                ),
                Button(
                    style = ButtonStyle.red,
                    custom_id = 'off',
                    label = 'Выключить',
                    emoji = '❌'
                )
            )
            manager = ActionRow(
                Button(
                    style = ButtonStyle.green,
                    custom_id = 'add',
                    label = 'Добавить',
                    emoji = '🥊',
                    disabled = True
                ),
                Button(
                    style = ButtonStyle.blurple,
                    custom_id = 'list',
                    label = 'Список',
                    disabled = True
                ),               
                Button(
                    style = ButtonStyle.red,
                    custom_id = 'remove',
                    label = 'Удалить',
                    emoji = '🎲',
                    disabled = True
                )
            )
            row = ActionRow(
                Button(
                    style = ButtonStyle.blurple,
                    custom_id = 'list',
                    label = 'Список',
                    emoji = '🎲',
                    disabled = True
                )
            )
            msg = await ctx.send(embed=embed, components = [power, manager])
            on_click = await msg.wait_for_button_click(timeout = 120)
            ch = self.client.get_channel(ctx.channel.id)
            for _ in range(1):
                if on_click.component.id == 'list':
                    embed = discord.Embed(
                        title = "🎱 |  Авто-Бан",
                        description = f"\n".join([id for ban in config['list']]),
                        color = 0xc01919
                    )
                    embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                    await on_click.respond(embed=embed)
                if on_click.component.id == 'add':
                    embed = discord.Embed(
                        title = "🎱 |  Авто-Бан",
                        description = "*Введите ID Пользователя!*",
                        color = 0xc01919
                    )
                    embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                    await on_click.respond(embed=embed)
                    id = await self.client.wait_for('message', check=lambda msg: msg.author == ctx.author)
                    bans = config.list('list')
                    bans.append(id.content)
                    bans = [item.strip().strip("'") for item in bans]
                    print(bans)
                    with open(db) as mode:
                        data = yaml.safe_load(mode)
                    data.update(dict(list = bans))
                    with open(db, 'wb') as mode:
                        yaml.safe_dump(
                            data, 
                            mode, 
                            default_flow_style=False, 
                            explicit_start=True, 
                            allow_unicode=True, 
                            encoding='utf-8'
                        )
                    mode.close()

                    embed = discord.Embed(
                        title = "🎱 |  Авто-Бан",
                        description = f"**Пользователь был успешно добавлен в черный список!**",
                        color = 0xc01919
                    )
                    embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                    await ch.send(embed=embed)
                if on_click.component.id == 'remove':
                    embed = discord.Embed(
                        title = "🎱 |  Авто-Бан",
                        description = "*Введите ID Пользователя!*",
                        color = 0xc01919
                    )
                    embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                    await on_click.respond(embed=embed)
                    id = await self.client.wait_for('message', check=lambda msg: msg.author == ctx.author)
                    if id in ...:
                        embed = discord.Embed(
                            title = "🎱 |  Авто-Бан",
                            description = f"**Пользователь был успешно удален из черного списка!**",
                            color = 0xc01919
                        )
                        embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                        await ch.send(embed=embed)
                    else:
                        embed = discord.Embed(
                            title = "🎱 |  Авто-Бан",
                            description = f"**Данный пользователь не находится в черном списке!**",
                            color = 0x490909
                        )
                        embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                        await ch.send(embed=embed)

                
                if on_click.component.id == 'on':
                    with open(db) as mode:
                        data = yaml.safe_load(mode)
                    data.update(dict(mode = True))
                    with open(db, 'wb') as mode:
                        yaml.safe_dump(
                            data, 
                            mode, 
                            default_flow_style=False, 
                            explicit_start=True, 
                            allow_unicode=True, 
                            encoding='utf-8'
                        )
                    mode.close()
                    embed = discord.Embed(
                        title = "🎱 |  Авто-Бан",
                        description = f"**Черный список успешно включен!**",
                        color = 0xc01919
                    )
                    embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                    await ch.send(embed=embed)
                if on_click.component.id == 'off':
                    with open(db) as mode:
                        data = yaml.safe_load(mode)
                    data.update(dict(mode = False))
                    with open(db, 'wb') as mode:
                        yaml.safe_dump(
                            data, 
                            mode, 
                            default_flow_style=False, 
                            explicit_start=True, 
                            allow_unicode=True, 
                            encoding='utf-8'
                        )
                    mode.close()
                    embed = discord.Embed(
                        title = "🎱 |  Авто-Бан",
                        description = f"**Черный список успешно выключен!**",
                        color = 0xc01919
                    )
                    embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                    await ch.send(embed=embed)"""

def setup(client):
    client.add_cog(blacklist(client))