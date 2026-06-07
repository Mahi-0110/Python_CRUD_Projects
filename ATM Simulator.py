def Atm():

    print("===BOB ATM===")
    balance = 1000
    while True:
        print("1)check balance\n2)deposit\n3)withdraw\n4)exit")
        option = int(input("Enter your option here:"))
        if option == 1:
            print(f"Available balance:{balance}")
        elif option ==2:
            deposit = int(input("Enter deposit Amount:"))
            balance = balance + deposit
            print(f"After Depositing Amount:{balance}")
            
        elif option ==3:
            withdraw = int(input("Enter Withdrawal amount:"))
            if withdraw <=balance:
                balance = balance - withdraw
                print("cash dispend successfully!")
                print(f"Your current balance:{balance}")
            else:
                print("insufficient Funds")
            
        elif option ==4:
            break
        else:
            print("invaild option")
            break
Atm()