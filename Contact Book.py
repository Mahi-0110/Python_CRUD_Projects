def contact_book():
    contacts = []
    while True:
        print("1)Add contact\n2)View contact\n3)search contact\n4)remove contact\n5)Exit")
        option = int(input("Enter option here:"))
        #add contact
        if option == 1:
            contact_add = input("Enter contact name:").lower()
            contacts.append(contact_add)
            print("Your contact saved successfully!")
        #view contact
        elif option == 2:
            if len(contacts)==0:
                print("You don't have contacts")
            else:
                for contact_view in contacts:
                    print(contact_view)
        #search contact            
        elif option == 3:
            contact_search = input("Enter contact:").lower()
            if contact_search in contacts:
                print("Contact found")
            else:
                print("Contact not found")
        #remove contact 
        elif option == 4:
            contact_remove = input("Enter contact:").lower()
            if contact_remove in contacts:
                contacts.remove(contact_remove)
                print("contact removed successfully!")
            else:
                print("Contact is not there")
        #exit
        elif option==5:
            break
        else:
            print("invaild option")

contact_book()

