import datetime

from os import listdir
from os.path import join, realpath, split, splitext

from discord import Intents
from discord.ext import commands
from discord.ext import tasks
from config import settings


client = commands.Bot(command_prefix = ['s.', 'S.'], intents=Intents.all())
client.remove_command('help')

"""
@tasks.loop(minutes=60)
async def deadchat():
    hour = datetime.datetime.today().strftime("%H")
    sleep = [
            21,
            23,
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8
            ]

    if hour in sleep:
        return
    else:
        channel = client.get_channel(997245771290247240)
        await channel.send("<@&997425504485384253>")

@client.event
async def on_ready():
    deadchat.start()
"""


for item in listdir(join(split(realpath(__file__))[0], "cogs")):
    if item.endswith(f'.py'):
        client.load_extension(f'cogs.{item[:-3]}')

client.run(settings['TOKEN'])


# C:/Users/алексей/AppData/Local/Programs/Python/Python38-32/python.exe "c:/файлы/Python Projects/MrSphericalBot/FullVersion/main.py"