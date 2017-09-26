from peewee import (CharField, ForeignKeyField, SqliteDatabase, Model,
                    OperationalError)


db = SqliteDatabase('contacts.db')


class contact_name(Model):
    name = CharField(primary_key=True)

    class Meta:
        database = db


class contact_number(Model):
    number = CharField()
    name = ForeignKeyField(contact_name)

    class Meta:
        database = db


def initialize_db():
    db.connect()
    try:
        db.create_table(contact_name)
    except OperationalError:
        print("Contact_name table already exists!")

    try:
        db.create_table(contact_number)
    except OperationalError:
        print("Contact_number table already exists!")

    # contact = contact_name.create(name="pooja")
    # contact.save()
    # contact = contact_number.create(name="pooja", number="9999999999")
    # contact.save()


def get_option():
    print()
    print("1. Add/Update a contact")
    print("2. Delete a contact")
    print("3. Print contact details")
    print("4. Print all contacts")
    print("5. Exit")
    return input("\nPlease enter your choice: ")


def do_add_update():

    iname = input("\nEnter Contact Name: ")
    inumber = input("Enter Contact Number: ")

    contact = contact_name.select().where(contact_name.name == iname)

    if not contact:
        contact = contact_name(name=iname)
        contact.save()
        print("Contact added successfully")
    else:
        print("Name already exist")

    contact = contact_number.select().where(contact_number.name == iname) and (
        contact_number.number == inumber)

    if not contact:
        contact = contact_number(name=iname, number=inumber)
        contact.save()
        print("Contact number added successfully")
    else:
        print("Name and number already exist")


def do_delete():

    name = input("\nEnter Contact Name: ")

    deletecontact = contact_name.contact_number.select().where(
        contact_name.name == name and (
            contact_name.name == contact_number.name))

    if not deletecontact:
        print("Name doesn't exist")
    else:
        contactdelete = contact_number.get(contact_number.name == name)
        contactdelete.delete_instance(recursive=True)
        print("Contact deleted successfully")


def display():

    name = input("\nEnter Contact Name: ")

    displayquery = contact_name.contact_number.select(
        contact_number.number).where(
        contact_name.name == name and (
            contact_name.name == contact_number.name).group_by(
            contact_name.name))
    print(displayquery)


def display_all():

    print("")

    """ for contact in contact_name.select(contact_name.name):
        print(contact.name + ":")
        for num in contact.select().where(contact.name == cont.name):
           print(num.number)
    """
