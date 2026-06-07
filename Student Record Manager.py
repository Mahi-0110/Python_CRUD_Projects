def student_record_manager():
    students=[]
    marks = []
    while True:
        print("1. Add Student\n2. View Students\n3. Search Student\n4. Delete Student\n5. Average Marks\n6. Topper\n7. Exit")
        option = int(input("Enter option:"))
        #add student
        if option == 1:
            name = input("enter student name:")
            mark = int(input("enter student marks:"))
            students.append(name)
            marks.append(mark)
        #view student
        elif option == 2:
            if len(students)==0:
                print("No student record is added")
            else:    
                for i in range(len(students)):
                    print(f"{students[i]}->{marks[i]}")
        #search student
        elif option == 3:
            search_name =input("Enter student name:")
            if search_name in students:
                print("Student found")
            else:
                print("Student not found")
        #delete student
        elif option == 4:
            delete_student= input("enter student name:")
            if delete_student in students:
                index = students.index(delete_student)
                students.pop(index)
                marks.pop(index)
            else:
                print("student is not found")
        #average of marks
        elif option == 5:
            total = 0
            for av_marks in marks:
                total = total+av_marks
            average = total/len(marks)
            print(f"average:{average}")
        #topper
        elif option == 6:
            highest=0
            for high in marks:
                if high>highest:
                    highest = high
                    index_topper=marks.index(highest)

            print(f"{students[index_topper]}->{highest}")
                
        #exit
        elif option == 7:
            break
        else:
            print("invalid option")
student_record_manager()






                