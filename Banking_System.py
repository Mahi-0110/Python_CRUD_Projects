class Bankaccount():
    def __init__(self,name,account_number,phone_number,balance,account_type,ifsc_code):
        self.name = name
        self.account_number=account_number
        self.phone_number=phone_number
        self.balance=balance
        self.account_type=account_type
        self.ifsc_code=ifsc_code
        self.transactions=[]
    def deposit(self,amount):
        if amount > 0:
            self.balance +=amount
            print(f"{amount} deposited successfully!")
            print(f"updated balance is:{self.balance}")
            self.transactions.append({"type":"deposit", "amount": amount})
        else:
            print("enter amount greater than zero")
    def withdraw(self,amount):
        if amount > 100 :
            if amount <= self.balance:
                self.balance-=amount
                print(f"{amount} withdrawn successfully!")
                print(f"remaning balance:{self.balance}")
                self.transactions.append({"type":"withdraw","amount":amount})
            else:
                print("insuffient funds")
        else:
            print("enter amount greater than 100")
    def transfer(self,receiver,amount):

        if amount>0:

            if sender!=receiver:
                self.balance -= amount
                receiver.balance+=amount
                self.transactions.append({"type":"debited","amount":amount})
                receiver.transactions.append({"type":"credited","amount":amount})
                print("Transaction is Successfully!")

            else:
                print("Same account cannot be transfered")

    def show_balance(self):
        print(f"Available Balance:{self.balance} ")
    def show_transaction(self):
        print(f"Transaction History:{self.transactions}")
        
        
class Bank():
    def __init__(self):
        self.accounts ={}

    def create_account(self):
        name = input("enter name:")
        self.account_number=int(input("enter account number"))
        phone_number=input("enter phone number:")
        self.balance=int(input("enter intial balance:"))
        self.account_type=input("enter account type:")
        self.ifsc_code=input("enter ifsc code:")
        account=Bankaccount(name,self.account_number,phone_number,self.balance,self.account_type,self.ifsc_code)
        if account.account_number in self.accounts:
            print("Account already exists")
        else:
            self.accounts[account.account_number] = account
            print("account created successfully")
        return account
    def find_account(self):
        account =int(input("enter account:"))
        if account in self.accounts:
            return self.accounts[account] 
            
        else:
            print("Account Not Found")
bank = Bank()
while True:
    print("=====Menu=====")
    print("1.Create Account\n2.Find Account\n3.Deposit\n4.Withdraw\n5.Transfer\n6.Show balance\n7.Show Transactions\n8.Exit")

    option = int(input("Enter your choice:"))
    if option == 1:
        bank.create_account()
        print("Thank you")
    elif option == 2:
        
        bank.find_account()
        print("Account found")
    elif option == 3:
        account = bank.find_account()
        if account :
            amount = int(input("enter amount:"))
            account.deposit(amount)
    elif option == 4:
        account=bank.find_account()
        if account:
            amount = int(input("enter amount:"))
            account.withdraw(amount)
    elif option ==5:
        sender = bank.find_account()
        receiver = bank.find_account()
        if sender and receiver:
            amount = int(input("Enter amount:"))
            sender.transfer(receiver,amount)
            
    elif option == 6:
        account=bank.find_account()
        if account:
            account.show_balance()
    elif option == 7:
        account = bank.find_account()
        if account:
            account.show_transaction()
    elif option == 8:
        
        print("Thank you")
        break
