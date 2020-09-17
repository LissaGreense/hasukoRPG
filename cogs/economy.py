from discord.ext import commands
from discord_service.bot import Bot
import random
import discord
import asyncio


class Economy(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @commands.command()
    async def check_money(self, ctx):
        user = ctx.author
        if self.bot.character_manager.if_user_have_character(user.id):
            content = self.bot.character_manager.get_character_field(user.id, "gold")
            await ctx.send("Your money: {}".format(content))
        else:
            await ctx.send("You don't have a character!".format(user.name))\
    
    
    @commands.command()
    @commands.cooldown(rate=1, per=3600, type=commands.BucketType.user)
    async def earn_money(self, ctx):
        user = ctx.author
        if self.bot.character_manager.if_user_have_character(user.id):
            money = int(self.bot.character_manager.get_character_field(user.id, "gold"))
            earned_money = random.randrange(10)
            await ctx.send("Your earned {}!".format(earned_money))
            self.bot.character_manager.update_character_field(user.id, "gold", str(earned_money+money))
        else:
            await ctx.send("You don't have a character!".format(user.name))


def setup(bot):
    bot.add_cog(Economy(bot))
