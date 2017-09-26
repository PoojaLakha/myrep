from db_operations import (initialize_db, do_add_update, get_option, do_delete,
                           display, display_all, db)

if __name__ == '__main__':

    initialize_db()

    option = get_option()

    while not option == "5":
        if option == "1":
            do_add_update()
        elif option == "2":
            do_delete()
        elif option == "3":
            display()
        elif option == "4":
            display_all()
        elif option not in['1', '2', '3', '4', '5']:
            print("Enter options only between 1 to 5")
        option = get_option()

    db.close()
