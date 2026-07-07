#function
def student_dictonary_manager():
    students = {}
    while True:
        print("1.Add student\n2.view student\n3.search student\n4.update marks\n5.delete students\n6.count students\n7.exit")
        option = int(input("Enter option here:"))
        #add students
        if option == 1:
            student_name = input("Enter student name:")
            student_marks = int(input("Enter student marks:"))
            students[student_name] = student_marks
            print("student added successfully!")
        #view students
        elif option == 2:
            for view in students:
                print(f"{view}->{students[view]}")
        #search students
        elif option == 3:
            student_search = input("Enter student name:")
            if student_search in students:
                print("Student found")
            else:
                print("Not found")
        #update marks
        elif option == 4:
            update_ = input("Enter student name:")
            update_marks = int(input("Enter student marks:"))
            if update_ in students:
                students[update_] = update_marks
                print("updated successfully")
            else:
                print("student not found")
        #delete student
        elif option == 5:
            delete_name = input("Enter name:")
            if delete_name in students:
                students.pop(delete_name)
                print("Deleted successfully!")
            else:
                print("No record founded")
        #to count students
        elif option == 6:
            print(f"counted students:{len(students)}")
        #to exit
        elif option == 7:
            break
        else:
            print("invalid option")

student_dictonary_manager()
