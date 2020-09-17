from .character_sheet import CharacterSheet
from constans.character_fields_constans import *
from database.database_manager import DatabaseManager


class CharacterManager:
	def __init__(self, database: DatabaseManager):
		self._database = database

	def create_new_character(self, character_data: dict, user_id: int) -> bool:
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
		new_sheet.set_default_money()
		
		if new_sheet.if_all_fields_filled():
			self._database.save_character_sheet(new_sheet, user_id)
			return True
		
		return False
	
	def if_user_have_character(self, user_id: int) -> bool:
		return self._database.if_user_have_character(user_id)
	
	def delete_character_sheet(self, user_id: int):
		self._database.delete_character_sheet(user_id)
	
	def get_character_data(self, user_id: int) -> CharacterSheet:
		downloaded_character = CharacterSheet()
		character_data = self._database.get_character_sheet(user_id)
		
		downloaded_character.set_name(character_data[1])
		downloaded_character.set_surname(character_data[2])
		downloaded_character.set_age(character_data[3])
		downloaded_character.set_sex(character_data[4])
		downloaded_character.set_sexual_orientation(character_data[5])
		downloaded_character.set_power(character_data[6])
		downloaded_character.set_personality(character_data[7])
		downloaded_character.set_appearance(character_data[8])
		downloaded_character.set_history(character_data[9])
		downloaded_character.set_money(int(character_data[10]))
		
		return downloaded_character
	
	def get_character_field(self, user_id: int, field_name: str) -> str:
		field_content = self._database.get_character_field(user_id, field_name)[0]
		return field_content
		
	def update_character_field(self, user_id: int, field_name: str, new_content: str):
		self._database.update_character_field(user_id, field_name, new_content)
