from discord_service.bot import Bot
from rpg_utils.character_manager import CharacterManager
import os


class Runner:
	def __init__(self, args):
		self._debug = args.debug
		self._token = args.token
	
	def run(self):
		if self._debug:
			print("Debug mode is turned on")
			
		character_manager = CharacterManager(None)
		discord_manager = Bot(character_manager, command_prefix='MG!', prefix='MG!', command_attrs=dict(hidden=True))
		
		for file in os.listdir("cogs"):
			if file.endswith(".py") and file != '__init__.py':
				name = file[:-3]
				discord_manager.load_extension(f"cogs.{name}")
		
		discord_manager.run(self._token)
