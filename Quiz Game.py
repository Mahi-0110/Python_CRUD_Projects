def quiz_game():
    questions = ["1)What is 5 + 5?","2)What is 10 - 3?","3) What is 4 * 2?","4)What is 12 / 3?"]
    answers = [10,7,8,4]
    
    while True :
        print("1)Start Quiz\n2)Show score\n3)exit")
        option = int(input("Enter option here:"))
        if option == 1:
            score=0
            for i in range(len(questions)):
                print(questions[i])
                answer = int(input("Enter answer:"))
            
                if answer == answers[i]:
                      
                        print("correct answer")
                        score = score+1
                else:
                        print("Incorrect answer")
        elif option == 2:
            print(f"Your score is:{score}")
        elif option == 3:
            break
        else:
            print("Invalid option")
quiz_game()