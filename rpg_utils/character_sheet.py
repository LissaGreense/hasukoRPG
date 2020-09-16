class CharacterSheet:
	def __init__(self):
		self.__name = str()
		self.__surname = str()
		self.__age = 0
		self.__sex = str()
		self.__sexual_orient = ''
		self.__power = str()
		self.__appearance = str()
		self.__personality = str()
		self.__history = str()

	@property
	def get_name(self):
		return self.__name

	@property
	def get_surname(self):
		return self.__surname
	
	@property
	def get_age(self):
		return self.__age
	
	@property
	def get_sex(self):
		return self.__sex
	
	@property
	def get_power(self):
		return self.__power
	
	@property
	def get_sexual_orientation(self):
		return self.__sexual_orient
	
	@property
	def get_appearance(self):
		return self.__appearance
	
	@property
	def get_personality(self):
		return self.__personality
	
	@property
	def get_history(self):
		return self.__history
	
	def set_name(self, val):
		if len(val) < 64:
			self.__name = val
		
	def set_surname(self, val):
		if len(val) < 128:
			self.__surname = val
		
	def set_age(self, val):
		self.__age = val
	
	def set_power(self, val):
		self.__power = val
	
	def set_sex(self, val):
		if len(val) > 32:
			self.__sex = val
		
	def set_sexual_orientation(self, val):
		self.__sexual_orient = val
		
	def set_personality(self, val):
		self.__personality = val
		
	def set_appearance(self, val):
		self.__appearance = val
		
	def set_history(self, val):
		self.__history = val
	
	def if_all_fields_filled(self):
		for field in vars(self):
			if not field:
				return False
		return True
