import config
import settings
from discord import Intents
from discord.ext import commands
from dislash import InteractionClient


client = commands.Bot(command_prefix = config.PREFIX, case_insensitive=True, intents=Intents.all())
client.remove_command('help')
InteractionClient(client)
line = '----------------------------------------------'


if __name__ == '__main__':
	for extension in settings.extensions.extensions:
		try:
			client.load_extension(extension)
		except Exception as e:
			print(f'{line}\n[!] Не удалось загрузить модуль {extension}.')
			print(f'[!] {e}\n{line}')
		else:
			print(f'[!] Модуль {extension} успешно загружен.')

client.run(config.TOKEN)


# python "E:/Python Projects/MrSphericalBot/FullVersion/main.py"