# Library Managment System
from pip import main

class Library:

    def __init__(self, list, name):
        self.listofBooks = list
        self.libraryName = name 
        self.lendDict = {}

    def displayBook(self):
        print(f"We have the following books in library : {self.libraryName}")
        for book in self.listofBooks:
            print(book)

    def lendBook(self, user, book):
        if book not in self.listofBooks:
            print("This book is not available right now.")
        else:
            if book not in self.lendDict.keys():
                self.lendDict.update({book:user})
                print("Database has been updated.")
            else:
                print(f'Book is already been taken by {self.lendDict[book]}')

    def addBook(self, book):
        self.listofBooks.append(book)
        print("Book has been added.")
        
    def returnBook(self, book):
        self.lendDict.pop(book)
        print("Book returned successfully.")

if __name__ == '__main__':
    ad = Library(['Harry Potter',"Lord of the Ring",'Book3 ','King in the North'],"Central Library")
    while(True):
        print(f"Welcome to {ad.libraryName}. Choose Command \n 1. Display Book \n 2. Lend Book \n 3. Add Book \n 4. Return Book\n")
        userChoice = input()
        if userChoice not in ["1","2","3","4","5"]:
            print("Enter a valid value!")
            continue
        else:
            userChoice = int(userChoice)

        if userChoice == 1:
            ad.displayBook()

        elif userChoice == 2:
            book = input("Enter the name of the book you want to lend : ")
            user = input("Enter your name : ")
            ad.lendBook(user,book)

        elif userChoice == 3:
            book = input("Enter the name of the book you want to add : ")
            ad.addBook(book)

        elif userChoice == 4:
            book = input("Enter the name of the book you want to return : ")
            ad.returnBook(book)
        elif userChoice == 5:
            print(ad.lendDict)

        else:
            print("Not a valid command")

        print("Press q to quit and c to continue")
        while(userChoice!="c" and userChoice!="q"):
            userChoice = input()
            if userChoice == "q":
                exit()
            if userChoice == "c":
                continue 
            else:
                print("Not a valid command")
