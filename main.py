import config
import settings

import asyncio
import discord
from discord import Intents
from discord.ext import commands

class Account():
	if config.CANARY:
		prefix = config.prefix.CANARY
		token = config.token.CANARY
	else:
		prefix = config.prefix.MAIN
		token = config.token.MAIN
class Setup(commands.Bot):
	def main(self):	
		self.remove_command('help')
		self.line = '----------------------------------------------'
	
	async def setup_hook(self):
		self.main()
		for extension in settings.extensions.cogs:
			try:
				await self.load_extension(extension)
			except Exception as e:
				print(f'{self.line}\n[!] Не удалось загрузить модуль {extension}.')
				print(f'[!] {e}\n{self.line}')
			else:
				print(f'[!] Модуль {extension} успешно загружен.')
		print(self.line)
		for extension in settings.extensions.handlers:
			try:
				await self.load_extension(extension)
			except Exception as e:
				print(f'{self.line}\n[!] Не удалось загрузить хендлер {extension}.')
				print(f'[!] {e}\n{self.line}')
			else:
				print(f'[!] Хендлер {extension} успешно загружен.')


client = Setup(
	status = discord.Status.online, 
	activity = discord.Streaming(name=f's.help', url='https://www.youtube.com/c/%D0%9C%D0%B8%D1%81%D1%82%D0%B5%D1%80%D0%A1%D1%84%D0%B5%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9'), 
	case_insensitive=True, 
	command_prefix=Account.prefix, 
	intents=Intents.all()
)
client.run(Account.token)