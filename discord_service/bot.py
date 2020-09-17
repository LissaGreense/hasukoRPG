from discord.ext.commands import AutoShardedBot
import logging


class Bot(AutoShardedBot):
	
	def __init__(self, character_manager, *args, **kwargs):
		self.character_manager = character_manager
		super().__init__(*args, **kwargs)

	async def on_message(self, msg):
		if not self.is_ready() or msg.author.bot:
			return
		
		await self.process_commands(msg)
	
	@staticmethod
	async def on_ready():
		logging.info("Connected to the Discord")
	
	@staticmethod
	async def on_disconnect():
		logging.info("Disconnected")
