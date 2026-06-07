def Library_management_system():
    books =[]
    while True:
        print("1)Add Book\n2)View Book\n3)Search Book\n4)Remove Book\n5)exit")
        option = int(input("Enter Your option:"))
        #To add books
        if option == 1:
            book = input("enter book:").lower()
            books.append(book)
            for book in books:
                print(book)
        #To View books
        elif option == 2:
            if len(books) == 0:
                print("No books are in library")
            else: 
                for book_view in books:   
                    print(book_view)
        #To search books
        elif option == 3:
            book_search = input("Enter book:").lower()
            if book_search in books:
                print("Book Founded")
            else:
                print("Book Not Founded")
        elif option == 4:
            book_remove= input("enter book:").lower()
            if book_remove in books:
                books.remove(book_remove)
                print("book removed successfully!")
            else:
                print("the book is not there in library")
        elif option == 5:
            break


Library_management_system()