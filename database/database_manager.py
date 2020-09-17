from .postgress import PostgresDatabase
from constans.database_constans import *
from rpg_utils.character_sheet import CharacterSheet


class DatabaseManager:
    def __init__(self, args):
        self.__db_settings = self.__get_settings(args)
        self.__service = PostgresDatabase(self.__db_settings)
        self.__prepare_database()
    
    @staticmethod
    def __get_settings(args):
        db_settings = dict()
        db_settings[PASSWORD] = args.password
        db_settings[NAME] = args.db_name
        db_settings[USER] = args.user
        
        return db_settings
    
    def __prepare_database(self):
        characters_tab = "{} NUMERIC PRIMARY KEY, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, " \
                         "{} TEXT, {} TEXT".format(USER_ID, CH_NAME, CH_SURNAME, CH_AGE, CH_SEX, CH_SEXUAL_ORIENTATION,
                                                   CH_POWER, CH_APPEARANCE, CH_PERSONALITY, CH_HISTORY)
        
        self.__service.create_table_if_not_exist(CHARACTERS, characters_tab)
    
    def save_character_sheet(self, ch_sheet: CharacterSheet, user_id: int):
        data = "'{}'".format(user_id)
        
        data += ", '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(ch_sheet.get_name, ch_sheet.get_surname,
                                                                                ch_sheet.get_age, ch_sheet.get_sex,
                                                                                ch_sheet.get_sexual_orientation,
                                                                                ch_sheet.get_power,
                                                                                ch_sheet.get_appearance,
                                                                                ch_sheet.get_personality,
                                                                                ch_sheet.get_history)
        self.__service.insert_data(CHARACTERS, data)
    
    def if_user_have_character(self, user_id: int) -> bool:
        if self.__service.get_from_table_where(CHARACTERS, "1", "{}='{}'".format(USER_ID, user_id)):
            return True
        
        return False
    
    def get_character_sheet(self, user_id: int) -> tuple:
        condition = "{}={}".format(USER_ID, user_id)
        
        return self.__service.get_from_table_where(CHARACTERS, "*", condition)
    
    def delete_character_sheet(self, user_id: int):
        self.__service.delete_data(CHARACTERS, "{}='{}'".format(USER_ID, user_id))
    
    def get_character_field(self, user_id: int, field: str) -> tuple:
        field_content = self.__service.get_from_table_where(CHARACTERS, field, "{}='{}'".format(USER_ID, user_id))
        print(field_content)
        return field_content
    
    def update_character_field(self, user_id: int, field_name: str, new_content: str):
        self.__service.update_in_table_where(CHARACTERS, field_name, new_content, "{}='{}'".format(USER_ID, user_id))
        
    def close(self):
        self.__service.close()
