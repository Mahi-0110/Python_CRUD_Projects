def phone_book():
    contact_ ={}
    while True:
        print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Number\n5. Delete Contact\n6. Count Contacts\n7. Exit")
        option = int(input("enter option here:"))
        if option == 1:
            contact = input("enter name:")
            contact_number = int(input("enter number:"))
            contact_[contact] = contact_number
        elif option == 2:
            for view in contact_:
                print(f"{view}->{contact_[view]}")
        elif option == 3:
            search_con =input("enter the contact:")
            if search_con in contact_:
                
                print("contact found")
                print(f"{search_con}->{contact_[search_con]}")
            else:
                print("contact not found")
        elif option == 4:
            update_ =input("enter contact name:")
            update_num = int(input("enter number:"))
            if update_ in contact_:
                contact_[update_] = update_num
                print("contact updated successfully!")
                print(f"{update_}->{contact_[update_]}")
            else:
                print("contact not found")
        elif option == 5:
            dele_name = input("enter contact:")
            if dele_name in contact_:
                contact_.pop(dele_name)
                print("contact deleted successfully")
            else:
                print("contact not found")        
        elif option == 6:
            print(f"count of contact:{len(contact_)}")

        elif option == 7:
            break
        else:
            print("please enter valid option")

phone_book()
