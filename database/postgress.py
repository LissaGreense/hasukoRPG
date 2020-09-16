from constans.database_constans import *
import psycopg2
import sys


def cursor_connection(command):
	def function_wrapper(*args, **kwargs):
		self = args[0]
		args = args[1:]
		with self.connection.cursor() as cursor:
			return command(self, cursor, *args, **kwargs)
	return function_wrapper


class PostgressDatabase:
	def __init__(self, db_settings):
		self.__db_name = db_settings[NAME]
		self.__user = db_settings[USER]
		self.__password = db_settings[PASSWORD]
		
		self.connection = self.connect()

	def connect(self):
		connection_string = "dbname={} user={} password={}".format(self.__db_name, self.__user, self.__password)
		try:
			print("Connected to database")
			return psycopg2.connect(connection_string)
		except psycopg2.OperationalError as e:
			print("Can't connect to database. Exiting...")
			sys.exit(1)
			
	def close(self):
		if self.connection:
			self.connection.close()
			
	@cursor_connection
	def create_table_if_not_exist(self, cursor, table_name: str, columns_and_types: str):
		command = """CREATE TABLE IF NOT EXISTS {} ({});""".format(table_name, columns_and_types)
		cursor.execute(command)
		self.connection.commit()
	
	@cursor_connection
	def update_in_table_where(self, cursor, table_name: str, column_name: str, value, condition: str):
		command = """UPDATE {} SET {}='{}' WHERE {};""".format(table_name, column_name, value, condition)
		cursor.execute(command)
		self.connection.commit()
		
	@cursor_connection
	def insert_data(self, cursor, table_name: str, data: str):
		cursor.execute("""INSERT INTO {} VALUES ({});""".format(table_name, data))
		self.connection.commit()
		
	@cursor_connection
	def delete_data(self, cursor, table_name: str, condition: str):
		cursor.execute("""DELETE FROM {} WHERE {};""".format(table_name, condition))
		self.connection.commit()
	
	@cursor_connection
	def get_from_table_where(self, cursor, table_name: str, column_name: str, condition: str) -> tuple:
		command = """SELECT {} FROM {} WHERE {};""".format(column_name, table_name, condition)
		cursor.execute(command)
		
		return cursor.fetchone()

	@cursor_connection
	def get_from_table(self, cursor, table_name: str, column_name: str) -> tuple:
		command = """SELECT {} FROM {};""".format(table_name, column_name)
		cursor.execute(command)
		
		return cursor.fetchall()
