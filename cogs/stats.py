import discord
import settings
from discord.ext import commands
from discord.ext import tasks
from pymongo import MongoClient
import asyncio
from config.config import mongoconf

cluster = MongoClient(mongoconf.uri)
db = cluster.db
collect = db.event

class stats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @tasks.loop(minutes = 45)
    async def stats(self):
        guild = self.client.get_guild(settings.misc.guild)

        bots = 0
        for member in guild.members:
            if member.bot: bots += 1
        all = guild.member_count
        members = all - bots

        uwmx = list(collect.find().sort("count", -1).limit(1))[0]
        if uwmx:
            user = guild.get_member(int(uwmx["_id"]))
            event_msg = f"🏆・{user.nick}"
        else: event_msg = "🏆・Нет победителей"

        all_ch = self.client.get_channel(settings.stats.all)
        member_ch = self.client.get_channel(settings.stats.members)
        bots_ch = self.client.get_channel(settings.stats.bots)
        boosts_ch = self.client.get_channel(settings.stats.boosts)
        boosts_count = guild.premium_subscription_count
        status_ch = self.client.get_channel(settings.stats.status)
        event_ch = self.client.get_channel(settings.stats.eventwin)

        onl = sum(member.status==discord.Status.online and not member.bot for member in guild.members)
        dnd = sum(member.status==discord.Status.dnd and not member.bot for member in guild.members)
        idle = sum(member.status == discord.Status.idle and not member.bot for member in guild.members)

        await discord.VoiceChannel.edit(all_ch, name=f"🤠・Всего: {all}")
        await discord.VoiceChannel.edit(member_ch, name=f"🎃・Участников: {members}")
        await discord.VoiceChannel.edit(bots_ch, name = f"👾・Ботов: {bots}")
        await discord.VoiceChannel.edit(boosts_ch, name=f"💎・Бустов: {boosts_count}")
        await discord.VoiceChannel.edit(event_ch, name = event_msg)
        await discord.VoiceChannel.edit(status_ch, name=f"🟢{onl} ⛔{dnd} 🌙{idle}")

    @commands.Cog.listener()
    async def on_ready(self):
        self.stats.start()

async def setup(client):
    await client.add_cog(stats(client))
