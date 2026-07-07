def expense_tracker():
    expenses ={}
    while True:
        print("1. Add Expense\n2. View Expenses\n3. Search Expense\n4. Update Expense\n5. Delete Expense\n6. Total Expenses\n7. Exit")
        option = int(input("Enter option here:"))
        if option == 1:
            item_name = input("enter item name:")
            expnesive = int(input("enter cost:"))
            expenses[item_name] = expnesive
            print("Item added successfully!")
        elif option == 2:
            if len(expenses) == 0:
                print("No items are added")
            else:
            
                for view in expenses:
                    print(f"{view}->{expenses[view]}")
        elif option == 3:
            search_item = input("enter item:")
            if search_item in expenses:
                print(f"{search_item}->{expenses[search_item]}")
                print("item found")
            else:
                print("Item not found")
        elif option == 4:
            update_item = input("enter item:")
            update_price=int(input("enter expense:"))
            if update_item in expenses:
                expenses[update_item]=update_price
                print("updated successfully!")
                print(f"{update_item}->{expenses[update_item]}")
            else:
                print("no item is found")
        elif option == 5:
            dele_name = input("enter item:")
            if dele_name in expenses: 
                expenses.pop(dele_name)           
                print("item deleted successfully")      
            else: print("item not found")
        elif option == 6:
            total = 0
            for i in expenses:
                total +=expenses[i]
            print(f"Total expenses:{total}")
        elif option == 7:
            break
        else:
            print("invalid option")
expense_tracker()
                