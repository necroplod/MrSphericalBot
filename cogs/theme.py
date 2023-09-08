import typing

import settings
import datetime
import discord
import asyncio
import random
import re
from discord.ext import commands
from discord import app_commands
from typing import Union, Literal, Optional
import openai
openai.api_key = settings.openai.key
openai.api_base = settings.openai.url
class theme(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @app_commands.command(name = "theme", description = "Определим тему разговора за вас!")
    async def theme(self, interaction: discord.Interaction):
        messages = []
        async for message in interaction.channel.history(limit=5):
            messages.append(message.content)
        await interaction.response.defer(ephemeral=True)
        chat_completion_resp = await openai.ChatCompletion.acreate(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "Твоя задача определять тему разговора по сообщениям который отправит пользователь. Формат ответа - **Тема разговора**: (здесь тема)"}, {"role": "user", "content": f"Сообщения из Discord сервера: 1) {messages[0]}\n 2) {messages[1]}\n 3) {messages[2]}\n 4) {messages[3]}\n 5) {messages[4]}\n"}])
        await interaction.followup.send(embed=discord.Embed(color=0xfc652c, description=chat_completion_resp['choices'][0]['message']['content']).set_footer(icon_url = settings.misc.avatar_url, text = settings.misc.footer))
        
async def setup(client):
    await client.add_cog(theme(client))
