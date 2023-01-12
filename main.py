from os import listdir
from os.path import join, realpath, split, splitext
from dislash import InteractionClient


from discord import Intents
from discord.ext import commands
from config import settings

client = commands.Bot(command_prefix = ['s.', 'S.'], intents=Intents.all())
client.remove_command('help')
InteractionClient(client)



for item in listdir(join(split(realpath(__file__))[0], "cogs")):
    if item.endswith(f'.py'):
        client.load_extension(f'cogs.{item[:-3]}')

client.run(settings['TOKEN'])


# C:/Users/алексей/AppData/Local/Programs/Python/Python38-32/python.exe "c:/файлы/Python Projects/MrSphericalBot/FullVersion/main.py"