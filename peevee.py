from peewee import *

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

	cont = contact(name=Name, number=int(Number))
	cont.save() 

def DoDelete():
	Name = input("\nEnter Contact Name: ")

	del_cont = contact.get(contact.name==Name)
	del_cont.delete_instance()

def Display():
	name = input("\nEnter Contact Name: ")

	for cont in contact.select().join(contact).where(contact.name == Name):
		print(contact.name, contact.number)
	
def DisplayAll():
	
	for cont in contact.select():
		print(contact.name, contact.number)

db = SqliteDatabase('contacts.db')

class contact(Model):
    name = CharField()
    number = IntegerField()

class Meta:
    database = db 

db.connect()

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