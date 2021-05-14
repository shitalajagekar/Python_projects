# Library project

class Library:
    def __init__(self,books):
        self.booklist = books
        self.copyBookList = books

    def availableBooks(self):
        print("---Available Books are:--- ")
        for i in self.booklist:
            print(i)

        return True

    def borrowBooks(self,bookname):
        if bookname in self.booklist:
            self.booklist.remove(bookname)
            print(f"You have borrowed {bookname} book.")
        return True

    def returnBooks(self, bookname):
        if bookname in self.copyBookList:
            self.booklist.append(bookname)
            print(f"You have returned the book : {bookname}. Thanks for using library!!!")
        else:
            print("Book name is incorrect.")

    


class Student:

    def requestBook(self):
        bookname= input("Enter the book name to borrow : ")
        return bookname

    def returnBook(self):
        bookname= input("Enter the book name to return : ")
        return bookname


if __name__ == "__main__":
    centralLibrary = Library(["Python"," C++","C", "Java" ,".Net", "Machine Learning","Algorithm"])
    stud1 = Student()
    message= """========= Welcome to Central Library========
                Choose following option :\n
                1. Available Book \n
                2. Borrow Book \n
                3. Return Book \n
                4. Exit \n
                """
    print(message)
    
    while (True):
                
        option = int(input("Enter the option :  "))

        if option == 1:
            centralLibrary.availableBooks()

        elif option == 2:
            centralLibrary.borrowBooks(stud1.requestBook())

        elif option == 3:
            centralLibrary.returnBooks(stud1.returnBook())

        elif option == 4:
            exit()
        else:
            print("Enter the proper option to continue......")

