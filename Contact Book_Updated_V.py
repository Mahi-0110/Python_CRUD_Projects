#function
def contact_book():
    contact_names = []
    contact_no = []
    while True:
        print("1.Add contact\n2.View contact\n3.Delete contact\n4.search\n5.Exit")
        option = int(input("Enter option here:"))


        #add contact
        if option == 1:
            contact_name = input("Enter name:")
            contact_number = input("Enter Number:")
            count = 0
            data_change = int(contact_number)#phone number string is changed to intger datatype 
            for c in contact_number:
                count =count+1
            while True:
                if count == 10:
                    contact_names.append(contact_name)

                    contact_no.append(data_change)
                    print("Contact saved successfully!")
                    break
                elif count>10:
                    print("enter only 10 digits")
                    break
                else:
                    print("Enter minimum 10 digits")
                    break

        #view contact
        elif option == 2:

                if len(contact_names) == 0:
                    print("No contacts are added")
            
                else:
                    try:
                        for view in contact_names:
                            index = contact_names.index(view)
                            print(f"{contact_names[index]}->{contact_no[index]}")
                    except IndexError:
                        pass

        #delete contact
        elif option == 3:
            delete_name = input("enter name:")
            if delete_name in contact_names:
                index_delete=contact_names.index(delete_name)
                contact_names.pop(index_delete)
                contact_no.pop(index_delete)
                print("contact is deleted successfully!")
            else:
                print("Contact is not there")
        #search
        elif option == 4:
            search_name = input("Enter name:")
            if search_name in contact_names:
                index_search = contact_names.index(search_name)
                print(f"{contact_names[index_search]}->{contact_no[index_search]}")
                print("contact found")
            else:
                print("contact is not found")

        #exit
        elif option == 5:
            break
        else:
            print("invalid option")
contact_book()
