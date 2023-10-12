from config import config
import settings
import cogs.ticket
import cogs.role
import cogs.info
import cogs.adm

import discord
from discord import Intents
from discord.ext import commands
from discord import app_commands

class Account():
	if config.CANARY:
		prefix = config.prefix.CANARY
		token = config.token.CANARY
		game = '/help'
	else:
		prefix = config.prefix.MAIN
		token = config.token.MAIN
		game = '/help'
class Setup(commands.Bot):
	def main(self):	
		self.remove_command('help')
		self.line = '----------------------------------------------'
	
	async def setup_hook(self):
		self.main()
		self.add_view(cogs.ticket.PersistentView())
		self.add_view(cogs.ticket.TicketClose())
		self.add_view(cogs.ticket.TicketPanel())
		self.add_view(cogs.ticket.TicketWait())
		self.add_view(cogs.role.CountryView())
		self.add_view(cogs.role.AccessView())
		self.add_view(cogs.role.GenderView())
		self.add_view(cogs.role.NotifyView())
		self.add_view(cogs.adm.RecruitView())
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
	activity = discord.Streaming(name=Account().game, url='https://www.youtube.com/c/%D0%9C%D0%B8%D1%81%D1%82%D0%B5%D1%80%D0%A1%D1%84%D0%B5%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9'),
	case_insensitive=True, 
	command_prefix=Account.prefix, 
	intents=Intents.all()
)
client.run(Account.token)