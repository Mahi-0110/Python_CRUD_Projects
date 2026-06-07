def expenses_tracker():
    expenses =[]
    while True:
        print("1)Add expenses\n2)view expenses\n3)total spendings\n4)highest expenses\n5)Exit")
        option = int(input("Enter option here:"))
        #add expenses
        if option == 1:
            expense = int(input("Enter expenses:"))
            expenses.append(expense)
            print("expenses added successfully!")
        #view expenses
        elif option == 2:
            if len(expenses) == 0:
                print("No expenses are added")
            else:
                for expenses_view in expenses:
                    print(expenses_view)
        #total spendings
        elif option == 3:
            total = 0
            for total_spending in expenses:
                total = total +total_spending
            print(f"Total spendings:{total}")
        elif option == 4:
            highest_expenses = 0
            if len(expenses) == 0:
                print("No expenses are added")
            else:
                for high in expenses:
                    if high > highest_expenses:
                        highest_expenses = high
                print(f"Highest expenses:{highest_expenses}")
        elif option == 5:
            break
        else:
            print("invalid option")
            
expenses_tracker()                 
