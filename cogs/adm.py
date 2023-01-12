import discord
from discord.ext import commands
from dislash import InteractionClient, ActionRow, Button, ButtonStyle

class adm(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def blacklist(self, ctx):       
        if ctx.message.author.id != 678632704874381334:
            embed = discord.Embed(
                title = "🎱 |  Авто-Бан",
                description = f"**У вас нет доступа к черному списку!**",
                color = 0xc01919
            )
            embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} © Created by blackhome7 | Все права защищены')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title = "🎱 |  Авто-Бан",
                description = f"",
                color = 0xc01919
            )
            embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} © Created by blackhome7 | Все права защищены')

            row = ActionRow(
                Button(
                    style = ButtonStyle.green,
                    custom_id = 'on',
                    emoji = '✔'
                ),
                Button(
                    style = ButtonStyle.red,
                    custom_id = 'off',
                    emoji = '❌'
                )
            )
            msg = await ctx.send(embed=embed, components = [row])
            on_click = await msg.wait_for_button_click(timeout = 120)
            ch = self.client.get_channel(ctx.channel.id)
            for _ in range(1):
                if on_click.component.id == 'on':
                    self.client.load_extension(f'cogs.blacklist')
                    embed = discord.Embed(
                        title = "🎱 |  Авто-Бан",
                        description = f"**Черный список успешно включен!**",
                        color = 0xc01919
                    )
                    embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} © Created by blackhome7 | Все права защищены')
                    await ch.send(embed=embed)
                if on_click.component.id == 'off':
                    self.client.unload_extension(f'cogs.blacklist')
                    embed = discord.Embed(
                        title = "🎱 |  Авто-Бан",
                        description = f"**Черный список успешно выключен!**",
                        color = 0xc01919
                    )
                    embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} © Created by blackhome7 | Все права защищены')
                    await ch.send(embed=embed)






def setup(client):
    client.add_cog(adm(client))