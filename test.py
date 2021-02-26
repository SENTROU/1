a = ["мясо","растения","насекомых","рыбу","людей",]
b = ["губка","мшанки","плоские черви","круглые черви","кольчатые черви","кишечнополостные","членистоногие","молюски","иглокожие","хордовые",]
s = ["млекопитающие","пресмыкающиеся","земноводное","насекомое","птица","рыба","паукообразное","человек",]
t = []
class animals (): 
	name = None 
	age = None
	food = None
	detachment = None
	type_ = None
	behavior = None
	animal_species= None
	notice = None
	def delete(self):
		self.name = None
		self.age = None
		self.food = None
		self.detachment = None
		self.type_ = None
		self.behavior = None
		self.animal_species = None
		self.add_notice = None
	def info(self):
		print(self.name)
		print(self.age)
		print(self.food)
		print(self.detachment)
		print(self.type_)
		print(self.behavior)
		print(self.animal_species)
		print(self.notice)
	def add(self , name , age , food , detachment , animal_species , type_ , behavior):

		self.name = name
		self.age = age
		if self.age >> 50 :
			self.age = "наверное оно мертво ему за 50 " 
		self.food = food
		if self.food not in a :
			self.food = "ошибка"
		self.detachment = detachment
		if self.detachment not in s:
			self.detachment = "ошибка"
		self.type_ = type_
		if self.type_ not in b :
			self.type_ = "ошибка"
		self.behavior = behavior
		self.animal_species = animal_species
	def add_name(self , name):
		self.name = name
	def add_age(self , age):
		self.age = age
	def add_food(self , food):
		self.food
	def add_detachment(self , detachment):
		self.detachment = detachment
	def add_animal_species(self ,animal_species):
		self.animal_species = animal_species
	def add_type(self , type_):
		self.type_= type_
	def add_behavior(self , behavior):
		self.behavior = behavior
	def add_notice(self , notice):
		self.notice = notice
		
print("список команд \n info \n add  add_name  add_age  add_food  add_behavior add_animal_species add_type  add_notice \n delete") 