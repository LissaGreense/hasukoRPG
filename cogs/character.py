from discord.ext import commands
from constans.character_fields_constans import *
import discord
import asyncio


class Character(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	async def new_character(self, ctx, user: discord.Member = None):
		def check(message: discord.Message):
			return message.channel == ctx.channel and message.author != ctx.me
		if user:
			await ctx.send("I'm creating a new character sheet for {}!".format(user.name))

			try:
				character_data = await self.ask_for_all_character_data(check, ctx)
			
			except asyncio.TimeoutError:
				await ctx.send("Sorry, it takes too long")
			else:
				answer = self.bot.character_manager.create_new_character(character_data)
				
				if answer:
					await ctx.send("Character Sheet has been created!")
		else:
			await ctx.send("Please, tag a user to create a character sheet for him/her!")
	
	async def ask_for_all_character_data(self, check, ctx):
		character_data = dict()
		await ctx.send("Provide a name:")
		name = await self.bot.wait_for('message', check=check, timeout=60.0)
		character_data[NAME] = name.content
		await ctx.send("Provide a surname:")
		surname = await self.bot.wait_for('message', check=check, timeout=60.0)
		character_data[SURNAME] = surname.content
		await ctx.send("Provide a age:")
		age = await self.bot.wait_for('message', check=check, timeout=60.0)
		character_data[AGE] = age.content
		await ctx.send("Provide a sex:")
		sex = await self.bot.wait_for('message', check=check, timeout=60.0)
		character_data[SEX] = sex.content
		await ctx.send("Provide a sexual orientation:")
		sex_orient = await self.bot.wait_for('message', check=check, timeout=60.0)
		character_data[SEX_ORIENT] = sex_orient.content
		await ctx.send("Provide a super power:")
		power = await self.bot.wait_for('message', check=check, timeout=60.0)
		character_data[POWER] = power.content
		await ctx.send("Provide a personality description:")
		personality = await self.bot.wait_for('message', check=check, timeout=60.0)
		character_data[PERSONALITY] = personality.content
		await ctx.send("Provide a appearance description:")
		appearance = await self.bot.wait_for('message', check=check, timeout=60.0)
		character_data[APPEARANCE] = appearance.content
		await ctx.send("Provide a history:")
		history = await self.bot.wait_for('message', check=check, timeout=60.0)
		character_data[HISTORY] = history.content
		return character_data


def setup(bot):
	bot.add_cog(Character(bot))
