from db_operations import (initialize_db, close_db, do_add_update, do_delete,
                           display, display_all)


def get_option():
    print()
    print("1. Add/Update a contact")
    print("2. Delete a contact")
    print("3. Print contact details")
    print("4. Print all contacts")
    print("5. Exit")
    return input("\nPlease enter your choice: ")


if __name__ == '__main__':

    initialize_db()

    option = get_option()

    while not option == "5":

        if option == "1":

            iname = input("\nEnter Contact Name: ")
            inumber = input("Enter Contact Number: ")

            do_add_update(iname, inumber)

            print("Contact added/updated successfully")

        elif option == "2":

            iname = input("\nEnter Contact Name: ")

            delete_status = do_delete(iname)

            if not delete_status:
                print("Contact does not exist to delete")
            else:
                print("Contact deleted successfully")

        elif option == "3":

            iname = input("\nEnter Contact Name: ")

            contact_number = display(iname)

            if not contact_number:
                print("No contact to display")
            else:
                for number in contact_number:
                    print(number)

        elif option == "4":

            all_contacts = display_all()
            for contact in all_contacts:
                print(contact, all_contacts[contact])

        elif option not in['1', '2', '3', '4', '5']:

            print("Enter options only between 1 to 5")

        option = get_option()

    close_db()
