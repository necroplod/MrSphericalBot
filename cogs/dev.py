import datetime
import discord
import settings
import aeval

from discord.ext import commands

class dev(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx, extensions):
        await self.client.load_extension(f'cogs.{extensions}')
        embed = discord.Embed(
            title = "",
            description = f"Ког **{extensions}** был успешно загружен!",
            color = 0x93ff15
        )
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, extensions):
        await self.client.unload_extension(f'cogs.{extensions}')
        embed = discord.Embed(
            title = "",
            description = f"Ког **{extensions}** был успешно отгружен!",
            color = 0xf64c6e
        )
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, extensions):
        await self.client.unload_extension(f'cogs.{extensions}')
        await self.client.load_extension(f'cogs.{extensions}')
        embed = discord.Embed(
            title = "",
            description = f"Ког **{extensions}** был успешно перезагружен!",
            color = 0xf64c6e
            
        )
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} | Все права защищены')
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send(f"```Shutdown {self.client.user.name} : {str(datetime.datetime.now())}```")
        await self.client.close()

    @commands.command(hidden=True)
    async def eval(self, ctx):
        if ctx.author.id != settings.misc.dev:
            pass
        else:
            standart_args = {
                "discord": discord,
                "commands": commands,
                "client": self.client,
                "ctx": ctx,
            }
            await ctx.send('Введите код для исполнения...', delete_after = 5)
            start = datetime.datetime.now()
            try:
                code = await self.client.wait_for('message', check=lambda msg: msg.author == ctx.author)
                compile = code.content
                compile = compile.replace('```', '')
                r = await aeval.aeval(f"""{compile}""", standart_args, {})
                ended = datetime.datetime.now() - start
                embed = discord.Embed(
                    title="🎯 | Успешно!",
                    description=f"Выполнено за: {ended}",
                    color=0x99ff99
                )
                embed.add_field(name=f'Входные данные:', value=f'`{compile}`')
                embed.add_field(name=f'Вывод:', value=f'`{str(r)}`')
                await ctx.send(embed=embed, delete_after = 5)
            except Exception as e:
                ended = datetime.datetime.now() - start
                embed = discord.Embed(
                    title=f"🎯 | При выполнении возникла ошибка",
                    description=f'**Ошибка:**\n```py\n{e}```', color=0xff0000
                )
                embed.add_field(name=f'Время:', value=f'`{ended}`')
                await ctx.send(embed=embed, delete_after = 5)

async def setup(client):
    await client.add_cog(dev(client))