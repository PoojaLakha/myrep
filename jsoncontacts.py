from collections import defaultdict
import json

def GetOption():
	print()
	print("1. Add/Update a contact")
	print("2. Delete a contact")
	print("3. Print contact details")
	print("4. Print all contacts")
	print("5. Exit")
	return input("\nPlease enter your choice: ")

def DoAddUpdate():
	name = input("\nEnter Contact Name: ")
	number = input("Enter Contact Number: ")

	if name in cont_list:
		cont_list[name].append(number)
		print("Contact is updated")
	else:
		cont_list[name] = [name]
		cont_list[name] = [number]
		print("Contact is added")


def DoDelete():
	name = input("\nEnter Contact Name: ")

	if name in cont_list:
		del cont_list[name]
		print("Contact is deleted")
	else:
		print("Contact does not exist to delete")

def Display():
	name = input("\nEnter Contact Name: ")

	if name in cont_list:
		print(name,cont_list[name])
	else:
		print("Contact not in list to display")

def DisplayAll():
	for contact in cont_list:
		print(contact,cont_list[contact])	

cont_list = defaultdict(list)
#cont_list = {'pooja': [9999999999],'lakha':[8888888888]}

with open('contacts.json', 'r') as f:
	cont_list = json.load(f)

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

if Option == '5':
	with open('contacts.json', 'w') as f:
		    f.write(json.dumps(cont_list))