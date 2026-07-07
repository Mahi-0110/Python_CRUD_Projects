def voting_system_():
    votes ={}
    while True:
        print("1. Vote\n2. View Votes\n3. Winner\n4. Exit")
        option = int(input("Enter option here:"))
        if option == 1:
            vote_name =input("Enter language:")
            if vote_name in votes:
                votes[vote_name]+=1
            else:
                votes[vote_name] = 1
        elif option == 2:
            for view in votes:
                print(f"{view}->{votes[view]}")
        elif option == 3:
            high=0
            for i in votes:
                votes[i]
                
                if votes[i]>high:
                    high = votes[i]
                    winner = i
            print(f"winner is {winner}->{high}")
                
        else:
            break 
            
            
voting_system_()
