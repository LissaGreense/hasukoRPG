from discord_service.bot import Bot
from rpg_utils.character_manager import CharacterManager
from database.database_manager import DatabaseManager
import logging
import os
import sys


class Runner:
	def __init__(self, args):
		self._token = args.token
		self._args = args
	
	def run(self):
		database = DatabaseManager(self._args)
		try:
			character_manager = CharacterManager(database)
			discord_manager = Bot(character_manager, command_prefix='MG!', prefix='MG!', command_attrs=dict(hidden=True))
			
			self.load_cogs(discord_manager)
			
			discord_manager.run(self._token)
			
		except KeyboardInterrupt:
			database.close()
			logging.warning("Exiting...")
			sys.exit(1)
	
	@staticmethod
	def load_cogs(discord_manager: Bot):
		for file in os.listdir("cogs"):
			if file.endswith(".py") and file != '__init__.py':
				name = file[:-3]
				logging.debug(file)
				discord_manager.load_extension(f"cogs.{name}")
