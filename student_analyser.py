marks = [] #marks = [45,85,65,95,75]
n = int(input("Enter Number of values:"))
for i in range(n):
    mark = int(input("Enter marks:"))
    marks.append(mark) 
print(f"Marks Entered:{marks}")
def student_ananlyser():
#Total Marks
    total_marks = 0
    for i in marks:
        total_marks +=i
    print(f"Total Marks:{total_marks}")
    #Number of Marks
    Number_of_marks = 0
    for i in marks:
        Number_of_marks+=1
    print(f"Number of Marks:{Number_of_marks}")
    #Highest Mark
    Highest_marks = marks[0]
    for i in marks:
        if i > Highest_marks:
            Highest_marks = i
    print(f"Highest Marks:{Highest_marks}")
    #Lowest Mark
    Lowest_marks = marks[0]
    for i in marks:
        if i < Lowest_marks:
            Lowest_marks = i
    print(f"Lowest Marks:{Lowest_marks}")
    #Average Mark
    Average = total_marks/Number_of_marks
    print(f"Average Marks:{Average}")
    #Count of Marks >= 75
    count = 0
    for i in marks:
        if i >=75:
            count +=1
            print(f"Count of Marks >=75:{count}")
    else:
        print("No Marks are greater than equal to 75")
    

    #Total of Marks >= 75
    total = 0
    for i in marks:
        if i >=75:
            total+=i
            print(f"Total of marks >=75:{total}")
    else:
        print("No Marks are greater than equal to 75")
    #Average of Marks >= 75
    for i in marks:
        if i>=75:
            Average= total/count
            print(f"Average of Marks >=75: {Average}")
    else:
        print("No number is greater than equal to 75")
student_ananlyser()