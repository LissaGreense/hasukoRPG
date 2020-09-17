from discord.ext import commands
from constans.character_fields_constans import *
from discord_service.bot import Bot
from rpg_utils.character_sheet import CharacterSheet
import discord
import logging
import asyncio


class Character(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @commands.command()
    async def new_character(self, ctx, user: discord.Member = None):
        def check(message: discord.Message):
            return message.channel == ctx.channel and message.author != ctx.me
        
        if user:
            if self.bot.character_manager.if_user_have_character(user.id):
                await ctx.send("{} have a character! You have to delete it to create another one.".format(user.name))
            else:
                await self.create_new_character_sheet(check, ctx, user)
        else:
            await ctx.send("Please, tag a user to create a character sheet for him/her!")
    
    async def create_new_character_sheet(self, check, ctx, user: discord.Member):
        await ctx.send("I'm creating a new character sheet for {}!".format(user.name))
        
        try:
            character_data = await self.ask_for_all_character_data(check, ctx)
        
        except asyncio.TimeoutError:
            await ctx.send("Sorry, it takes too long")
        
        else:
            answer = self.bot.character_manager.create_new_character(character_data, user.id)
            if answer:
                await ctx.send("Character Sheet has been created!")
    
    async def ask_for_all_character_data(self, check, ctx) -> dict:
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
        
        logging.info("New character sheet data saved")
        logging.debug("Content: {}".format(character_data))
        
        return character_data
    
    @commands.command()
    async def show_character(self, ctx, user: discord.Member = None):
        if user:
            if self.bot.character_manager.if_user_have_character(user.id):
                await self.get_character_and_send(ctx, user)

            else:
                await ctx.send("This user doesn't have a character!")
        else:
            await ctx.send("Please, tag a user to show his/her character sheet!")

    async def get_character_and_send(self, ctx, user: discord.Member):
        ch_sheet = self.bot.character_manager.get_character_data(user.id)
        msg = await self.create_full_sheet_msg(ch_sheet)
        msg_chunks = await self.split_msg_into_chunks(msg)
        for chunk in msg_chunks:
            await ctx.send(chunk)

    @staticmethod
    async def split_msg_into_chunks(msg):
        max_chunk_length = 2500
        msg_chunks = [msg[i:i + max_chunk_length] for i in range(0, len(msg), max_chunk_length)]
        return msg_chunks
    
    @staticmethod
    async def create_full_sheet_msg(ch_sheet: CharacterSheet) -> str:
        msg = "Name: {}\n".format(ch_sheet.get_name)
        msg += "Surname: {}\n" .format(ch_sheet.get_surname)
        msg += "Age: {}\n".format(ch_sheet.get_age)
        msg += "Sex: {}\n".format(ch_sheet.get_sex)
        msg += "Sexual Orientation: {}\n".format(ch_sheet.get_sexual_orientation)
        msg += "Super Power: {}\n".format(ch_sheet.get_power)
        msg += "Appearance: {}\n".format(ch_sheet.get_appearance)
        msg += "Personality: {}\n".format(ch_sheet.get_personality)
        msg += "History: {}\n".format(ch_sheet.get_history)

        return msg

    @commands.command()
    async def delete_character(self, ctx, user: discord.Member = None):
        if user:
            if self.bot.character_manager.if_user_have_character(user.id):
                await self.get_character_and_send(ctx, user)
                await self.ask_and_delete(ctx, user)
            else:
                await ctx.send("This user doesn't have a character")
        else:
            await ctx.send("Please, tag a user to delete his/her character sheet!")

    async def ask_and_delete(self, ctx, user: discord.Member):
        def check(message: discord.Message):
            return message.channel == ctx.channel and message.author != ctx.me
        
        await ctx.send("Do you want to delete this character? (type: YES) ".format(user.name))
        sure = await self.bot.wait_for('message', check=check, timeout=60.0)
        if sure.content == "YES":
            self.bot.character_manager.delete_character_sheet(user.id)
            await ctx.send("{}'s character has been removed.".format(user.name))
        else:
            await ctx.send("{}'s character won't be removed.".format(user.name))
    
    @commands.command()
    async def edit_character(self, ctx, field: str, user: discord.Member = None):
        # TODO: do it better :/
        if user:
            if self.bot.character_manager.if_user_have_character(user.id):
                fields = [NAME, SURNAME, AGE, SEX, SEX_ORIENT, POWER, PERSONALITY, APPEARANCE, HISTORY]
                if field:
                    if field in fields:
                        old_content = self.bot.character_manager.get_character_field(user.id, field)
                        new_content = await self.ask_for_a_new_content(ctx, field, old_content)
        
                        self.bot.character_manager.update_character_field(user.id, field, new_content)
                    else:
                        await ctx.send("Choose one from available fields [{}]".format(', '.join(fields)))
                else:
                    await ctx.send("Provide a filed:{}".format(', '.join(fields)))
            else:
                await ctx.send("This user doesn't have a character")
        else:
            await ctx.send("Please, tag a user to edit his/her character sheet!")
    
    async def ask_for_a_new_content(self, ctx, field: str, old_content) -> str:
        def check(message: discord.Message):
            return message.channel == ctx.channel and message.author != ctx.me
    
        await ctx.send("{}:\n{}".format(field, old_content))
        await ctx.send("Write a new content for this filed:")
        new_content = await self.bot.wait_for('message', check=check, timeout=60.0)
        
        return new_content.content

    @commands.command()
    async def character_field(self, ctx, field: str, user: discord.Member = None):
        if user:
            if self.bot.character_manager.if_user_have_character(user.id):
                fields = [NAME, SURNAME, AGE, SEX, SEX_ORIENT, POWER, PERSONALITY, APPEARANCE, HISTORY]
                if field:
                    if field in fields:
                        content = self.bot.character_manager.get_character_field(user.id, field)
                        await ctx.send("{}:\n{}".format(field, content))
                    else:
                        await ctx.send("Choose one from available fields [{}]".format(', '.join(fields)))
                else:
                    await ctx.send("Provide a filed! [{}]".format(', '.join(fields)))
            else:
                await ctx.send("This user doesn't have a character")
        else:
            await ctx.send("Please, tag a user to edit her/his character sheet!")


def setup(bot):
    bot.add_cog(Character(bot))
