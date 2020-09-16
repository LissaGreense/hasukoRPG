from .character_sheet import CharacterSheet
from constans.character_fields_constans import *


class CharacterManager:
	def __init__(self, database):
		self._database = database

	def create_new_character(self, character_data) -> bool:
		new_sheet = CharacterSheet()
		
		new_sheet.set_name(character_data[NAME])
		new_sheet.set_surname(character_data[SURNAME])
		new_sheet.set_age(character_data[AGE])
		new_sheet.set_sex(character_data[SEX])
		new_sheet.set_sexual_orientation(character_data[SEX_ORIENT])
		new_sheet.set_power(character_data[POWER])
		new_sheet.set_personality(character_data[PERSONALITY])
		new_sheet.set_appearance(character_data[APPEARANCE])
		new_sheet.set_history(character_data[HISTORY])
		
		if new_sheet.if_all_fields_filled():
			return True
		
		return False
