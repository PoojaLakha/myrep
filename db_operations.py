from collections import defaultdict

from peewee import (CharField, ForeignKeyField, SqliteDatabase, Model,
                    OperationalError)


DB = SqliteDatabase('contacts.db')


class ContactName(Model):
    name = CharField(primary_key=True)

    class Meta:
        database = DB


class ContactNumber(Model):
    number = CharField()
    name = ForeignKeyField(ContactName)

    class Meta:
        database = DB


def initialize_db():
    DB.connect()
    try:
        DB.create_table(ContactName)
    except OperationalError:
        pass

    try:
        DB.create_table(ContactNumber)
    except OperationalError:
        pass


def close_db():
    DB.close()


def do_add_update(iname, inumber):

    ContactName.get_or_create(name=iname)
    ContactNumber.get_or_create(name=iname, number=inumber)


def do_delete(iname):

    contact_found = ContactName.select().where(
        ContactName.name == iname).first()

    if not contact_found:
        return False
    else:
        delete_contact = ContactName.select().where(
            ContactName.name == iname)
        ContactNumber.delete().where(ContactNumber.name.in_(
            delete_contact)).execute()

        ContactName.get(ContactName.name == iname)
        contact_found.delete_instance()
        return True


def display(iname):

    contact_list = []
    contact_present = False

    for display_contact in ContactNumber.select().where(
            ContactNumber.name == iname):
        if display_contact:
            contact_present = True
            contact_list.append(display_contact.number)

    return contact_list, contact_present


def display_all():

    all_contacts = defaultdict(list)

    for display_name in ContactName.select():
        for display_number in ContactNumber.select().where(
                ContactNumber.name == display_name.name):
            all_contacts[display_name.name].append(display_number.number)

    return all_contacts
