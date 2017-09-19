from peewee import *

def initialize_db():
	db.connect()
	try:
		db.create_table(contact)
	except OperationalError:
		print("Contact table already exists!")

def GetOption():
	print()
	print("1. Add/Update a contact")
	print("2. Delete a contact")
	print("3. Print contact details")
	print("4. Print all contacts")
	print("5. Exit")
	return input("\nPlease enter your choice: ")

def DoAddUpdate():

	Name = input("\nEnter Contact Name: ")
	Number = input("Enter Contact Number: ")

	cont = contact.select().where(contact.name == Name and contact.number == Number).first()

	if not cont:
		cont = contact(name=Name, number=int(Number))
		cont.save()
		print("Contact added successfully")
	else:
		print("Name and number already exist")

def DoDelete():
	Name = input("\nEnter Contact Name: ")
	Number = input("Enter Contact Number: ")

	del_cont = contact.select().where(contact.name==Name and contact.number==Number).first()

	if not del_cont:
		print("Name and(or) number does not exist, check again(using option 3 or 4)")
	else:
		contact.get(contact.name==Name and contact.number==Number)
		del_cont.delete_instance()
		print("Contact deleted successfully")

def Display():

	Name = input("\nEnter Contact Name: ")

	print(Name)

	for cont in contact.select().where(contact.name == Name):
		print(cont.number)

def DisplayAll():
	
	for cont in contact.select(contact.name).distinct():
		print(cont.name+":")
		for num in contact.select().where(contact.name == cont.name):
			print(num.number)
		print("")

db = SqliteDatabase('contacts.db')

class contact(Model):
    name = CharField()
    number = IntegerField()
    class Meta:
    	database = db 

initialize_db()
#cont = contact.create(name = "pooja", number = 9696969696)
#cont.save()

Option = GetOption()

while not Option == "5":
	if Option == "1":
		DoAddUpdate()
	elif Option == "2":
		DoDelete()
	elif Option == "3":
		Display()
	elif Option == "4":
		DisplayAll()
	elif Option not in['1','2','3','4','5']:
		print("Enter options only between 1 to 5")
	Option = GetOption()
 
db.close()