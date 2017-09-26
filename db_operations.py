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

    contact_name.get_or_create(name=iname)

    contact_number.get_or_create(name=iname, number=inumber)

    print("Contact details added/updated successfully")


def do_delete():

    iname = input("\nEnter Contact Name: ")

    deletecontact = contact_name.select().where(
        contact_name.name == iname).first()

    if not deletecontact:
        print("Contact doesn't exist")
    else:
        for contactdelete in contact_number.select().where(
                contact_number.name == iname):
            contactdelete.delete_instance()
        contact_name.get(contact_name.name == iname)
        deletecontact.delete_instance()
        print("Contact deleted successfully")


def display():
    Contact_present = False
    iname = input("\nEnter Contact Name: ")

    for displaycontact in contact_number.select().where(
            contact_number.name == iname):
        Contact_present = True
        print(displaycontact.number)
    else:
        if not Contact_present:
            print("No contacts to display")


def display_all():

    for displayname in contact_name.select():
        print(displayname.name + ":")
        for displaynumber in contact_number.select().where(
                contact_number.name == displayname.name):
            print(displaynumber.number)
        print("")
