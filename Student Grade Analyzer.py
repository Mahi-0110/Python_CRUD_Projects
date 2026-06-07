def student_grade():
    marks = []
    n = int(input("Enter number of mark:"))

    for i in range(n):
        mark = int(input("Enter Your marks:"))
        marks.append(mark)

    #Grade comparision 
    for i in marks:
        grade = ""
        if i >= 90:
            grade = "A"
            print(f"{i}->{grade}")
        elif i>=80:
            grade = "B"
            print(f"{i}->{grade}")
        elif i>=70:
            grade = "C"
            print(f"{i}->{grade}")
        elif i>=60:
            grade = "D"
            print(f"{i}->{grade}")
        else:
            grade = "F"
            print(f"{i}->{grade}")
    #count 
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    f_count = 0
    for i in marks :
        if i >= 90:
            a_count +=1
        elif i >=80:
            b_count +=1
        elif i >=70:
            c_count +=1     
        elif i>=60:
            d_count +=1       
        else:
            f_count +=1
            
    print(f"Count of A:{a_count}")
    print(f"Count of B:{b_count}")
    print(f"Count of C:{c_count}")
    print(f"Count of D:{d_count}")
    print(f"Count of F:{f_count}")
    pass_student = 0
    failed_student=0
    for i in marks:
        if i >=60:
            pass_student = pass_student+1
    print(f"passed students:{pass_student}")
    for i in marks:
        if i<60:
            failed_student = failed_student+1
    print(f"failed_students:{failed_student}")
student_grade()