import discord
import settings
from discord.ext import commands
from discord.ext import tasks

class stats(commands.Cog):

    def __init__(self, client):
        self.client = client


    @tasks.loop(minutes = 15)
    async def stats(self):
        guild = self.client.get_guild(settings.misc.guild)

        bots = 0
        for member in guild.members:
            if member.bot:
                bots += 1

        all = guild.member_count
        members = guild.member_count - bots

        all_ch = self.client.get_channel(settings.stats.all)
        member_ch = self.client.get_channel(settings.stats.members)
        bots_ch = self.client.get_channel(settings.stats.bots)
        boosts_ch = self.client.get_channel(settings.stats.boosts)
        boosts_count = guild.premium_subscription_count

        await discord.VoiceChannel.edit(all_ch, name=f"🤠・Всего: {all}")
        await discord.VoiceChannel.edit(member_ch, name=f"🎃・Участников: {members}")
        await discord.VoiceChannel.edit(bots_ch, name = f"👾・Ботов: {bots}")
        await discord.VoiceChannel.edit(boosts_ch, name=f"💎・Бустов: {boosts_count}")

    @tasks.loop(minutes = 50)
    async def stats_rp(self):
        guild = self.client.get_guild(settings.misc.guild_rp)
        bots = 0
        for member in guild.members:
            if member.bot:
                bots += 1

        members = guild.member_count - bots

        all_rp = self.client.get_channel(settings.stats.all_rp)
        member_rp = self.client.get_channel(settings.stats.members_rp)

        await discord.VoiceChannel.edit(all_rp, name=f"🤠・Всего: {guild.member_count}")
        await discord.VoiceChannel.edit(member_rp, name=f"🎃・Участников: {members}")

    @commands.Cog.listener()
    async def on_ready(self):
        self.stats.start()
        self.stats_rp.start()

async def setup(client):
    await client.add_cog(stats(client))