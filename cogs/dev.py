import datetime
import discord
import settings

from discord.ext import commands

class dev(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx, extensions):
        await self.client.load_extension(f'cogs.{extensions}')
        embed = discord.Embed(
            title='🎲 | Панель Управления',
            description=f'<a:768563657390030971:1041076662546219168>  *Ког {extensions} загружен успешно!*',
            color=0xcdc9a5
        )
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, extensions):
        await self.client.unload_extension(f'cogs.{extensions}')
        embed = discord.Embed(
            title='🎲 | Панель Управления',
            description=f'<a:768563657390030971:1041076662546219168>  *Ког {extensions} отгружен успешно!*',
            color=0xcdc9a5
        )
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, extensions):
        await self.client.unload_extension(f'cogs.{extensions}')
        await self.client.load_extension(f'cogs.{extensions}')
        embed = discord.Embed(
            title='🎲 | Панель Управления',
            description=f'<a:768563657390030971:1041076662546219168>  *Ког {extensions} перезагружен успешно!*',
            color=0xcdc9a5
        )
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        embed = discord.Embed(
            title='🎲 | Панель Управления',
            description=f'<a:768563657390030971:1041076662546219168>  **Бот выключается..*',
            color=0xcdc9a5
        )
        embed.set_footer(icon_url=self.client.user.avatar.url, text=f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)
        await self.client.close()

    @commands.command(hidden=True)
    @commands.is_owner()
    async def restart(self, ctx):
        embed = discord.Embed(
            title='🎲 | Панель Управления',
            description=f'<a:768563657390030971:1041076662546219168>  *Бот перезагружен успешно!*',
            color=0xcdc9a5
        )
        embed.set_footer(icon_url=self.client.user.avatar.url, text=f'{self.client.user.name} | Все права защищены')

        try:
            for extension in settings.extensions.cogs:
                await self.load_extension(extension)
            for extension in settings.extensions.handlers:
                await self.load_extension(extension)
        except: ...

        wilds = self.client.get_channel(settings.channels.wilds)
        await wilds.send('sync', delete_after = 1)

        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def sync(self, ctx):
        embed = discord.Embed(
            title='🎲 | Панель Управления',
            description=f'<a:768563657390030971:1041076662546219168>  *Слэш-команды успешно синхронизированы!*',
            color=0xcdc9a5
        )
        embed.set_footer(icon_url=self.client.user.avatar.url, text=f'{self.client.user.name} | Все права защищены')

        wilds = self.client.get_channel(settings.channels.wilds)
        await wilds.send('sync', delete_after = 1)

        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    async def adm(self, ctx):
        c = [f"<@{m.id}>" for m in ctx.guild.members if m.guild_permissions.administrator]
        c2 = [f"<@{m.id}>" for m in ctx.guild.members if m.guild_permissions.ban_members]
        c3 = [f"<@{m.id}>" for m in ctx.guild.members if m.guild_permissions.kick_members]
        c4 = [f"<@{m.id}>" for m in ctx.guild.members if m.guild_permissions.manage_channels]
        c5 = [f"<@{m.id}>" for m in ctx.guild.members if m.guild_permissions.manage_guild]
        c6 = [f"<@{m.id}>" for m in ctx.guild.members if m.guild_permissions.manage_roles]
        c7 = [f"<@{m.id}>" for m in ctx.guild.members if m.guild_permissions.manage_webhooks]

        embed = discord.Embed(
            title = "🥌 | Права",
            description = f"*Администратор* — {c}\n\n*Бан* — {c2}\n\n*Кик* — {c3}\n\n*Управление каналами* — {c4}\n\n*Управление сервером* — {c5}\n\n*Управление ролями* — {c6}\n\n*Управление вебхуками* — {c7}",
            color = 0xa0f1bc
        )
        embed.set_footer(icon_url=self.client.user.avatar.url, text=f'{self.client.user.name} | Все права защищены')

        await ctx.send(embed=embed)



async def setup(client):
    await client.add_cog(dev(client))