import settings

import re
import discord
import base64
from discord.ext import commands

class rp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = self.client.get_channel(message.channel.id)

        if message.channel.id == settings.channels.rp:
            if message.author.bot:
                return
            else:
                if message.content.startswith('^'):
                    return
                else:
                    embed_raw = discord.Embed(
                        title = "🎲 | Анонимный чат",
                        description = f'```{message.content}```',
                        timestamp = message.created_at,
                        color = 0x6ae8cd
                    )
                    embed_raw.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                    await message.delete()
                    msg1 = await channel.send(embed=embed_raw)
                    authorid = message.author.id
                    msgid = msg1.id
                    ch = message.channel.id
                    chksum = settings.misc.rp

                    code_raw = f'''[id]{authorid}[id]
[msg]{msgid}[msg]
[ch]{ch}[ch]
[chksum]{chksum}[chksum]
'''
                    code_bytes = code_raw.encode('utf-8')
                    code = base64.b64encode(code_bytes)
                    code = str(code)
                    code = code.replace("b'", "")
                    code = code.replace("'", "")

                    embed = discord.Embed(
                        title = "🎲 | Анонимный чат",
                        description = f'```{message.content}```\n\n**Секретный код:** ||{code}||',
                        timestamp = message.created_at,
                        color = 0x6ae8cd
                    )
                    embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                    await msg1.edit(embed=embed)

        else:
            return
    
    @commands.command()
    @commands.has_any_role(952530469751255043, 952530469751255042, 952530469751255041, 997425466254307369, 997425464807280681)
    async def minfo(self, ctx, hash_raw):
        try:
            code_raw = hash_raw.encode('utf-8')
            code = base64.b64decode(code_raw)
            code = code.decode('utf-8')

            author = re.search(r'\[id](.*)\[id]', code, re.DOTALL).group(1)
            msg = re.search(r'\[msg](.*)\[msg]', code, re.DOTALL).group(1)
            ch = re.search(r'\[ch](.*)\[ch]', code, re.DOTALL).group(1)

            msg_ch = self.client.get_channel(int(ch))
            msg_content = await msg_ch.fetch_message(msg)
            embeds = msg_content.embeds
            for embed_content in embeds:
                full = embed_content.to_dict()
            dscrpt_raw = full['description']
            dscrpt = re.search(r'\```(.*)\```', dscrpt_raw, re.DOTALL).group(1)
            
            def chksum(self, hash):
                if settings.misc.rp in hash:
                    return True
                else:
                    return False  
            if chksum(self, hash = code): 
                embed = discord.Embed(
                    title = '🥏 | Декодер',
                    description = f'''
                    **Автор:** <@{author}> | `{author}`
                    **Канал:** <#{ch}> | `{ch}`
                    **Сообщение:** `{dscrpt}` | `{msg}`''',
                    color = 0x51a944
                    )
                embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                await ctx.send(embed=embed)
            else:           
                embed = discord.Embed(
                    title = '🥏 | Декодер',
                    description = '**Контрольная сумма неверна, возможно код поврежден.**',
                    color = 0x490909
                )
                embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                await ctx.send(embed=embed)
        except Exception as e:
                embed = discord.Embed(
                    title = '🥏 | Декодер',
                    description = f'''**Произошла ошибка, скорее всего оригинальное сообщение не было найдено.**\n\n**Ошибка:** ||{e}||''',
                    color = 0x51a944
                )
                embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                await ctx.send(embed=embed)

        """
        if hash_raw.startswith("b'"): 
            code = base64.b64decode(hash_raw)
            code = code.decode('utf-8')
            author = re.search(r'\[id](.*)\[id]', code, re.DOTALL).group(1)
            msg = re.search(r'\[msg](.*)\[msg]', code, re.DOTALL).group(1)
            ch = re.search(r'\[ch](.*)\[ch]', code, re.DOTALL).group(1)
            if chksum(self, hash = code):
                embed = discord.Embed(
                    title = '🥏 | Декодер',
                    description = f'''
                    **Автор:** <@{author}>
                    **ID Сообщения:** {msg}
                    **ID Канала:** {ch}''',
                    color = 0x51a944
                )
                embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title = '🥏 | Декодер',
                    description = '**Контрольная сумма неверна, возможно код поврежден.**',
                    color = 0x490909
                )
                embed.set_footer(icon_url = self.client.user.avatar_url, text = f'{self.client.user.name} | Все права защищены')
                await ctx.send(embed=embed)
        else:
"""
    



def setup(client):
    client.add_cog(rp(client))