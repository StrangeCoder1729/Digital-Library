import time
from datetime import datetime

class Addingbooks:
    def __init__(self,books):
        self.books = books
    
    @property
    def adding (self):
        with open("library.txt","a") as f:
            f.write(f"{self.books}\n")

class Removingbooks(Addingbooks):

    @property
    def removal(self):
        lst_old = []
        lst_new = []
        
        with open ("library.txt","r+") as f:
            l = f.readlines()
            for i in l:
                lst_old.append(i)
            # print(lst_old)
            # m = len(lst_old)
            # print(lst_old.index(f"{self.books}\n"))
            for i in lst_old:
                if(f"{self.books}\n" in lst_old):
                    lst_old.remove(f"{self.books}\n")
                    # print("All Working")
            # print(f"new list : {lst_old}")
            for letter in lst_old:
                lst_new.append(letter)
            # print(lst_new)

        with open("library.txt","wt") as f:
            for letter in lst_new:
                f.write(letter)

class SeeingBooks:

    @property
    def viewing(self):
        with open("library.txt","rt") as f:
            print(f.read())

class Logs:

    @property
    def whole_hist(self):
        with open("logs.txt","rt") as f:
          print(f.read())
    
    @property
    def donating(self):
        with open("donated_books.txt","rt") as f:
            print(f.read())

    @property
    def borrowed_hist(self):
        with open("borrowed_books.txt","rt") as f:
            print(f.read())





try:
    print("Welcome to Books Library")
    print(" ")
    print("Actions :-")
    print("(1) Donating Books")
    print("(2) Borrowing Books")
    print("(3) Viewing the Library")
    print("(4) Seeing the history")
    print(" ")
    choice = int(input("Which are the actions do you like to execute (serial number): "))
    
 
    if(choice == 1): 
        try:
            user = input("Enter your full name : ")
            string1 = input("Enter the name of the book you want to donate : ")
            action1 = Addingbooks(string1)
            action1.adding
            with open("logs.txt","a") as f:
                presentime = datetime.now()
                f.write(f"[{presentime}] : {user} donated {string1}\n")      
            with open("donated_books.txt","a") as f:
                presentime = datetime.now()
                f.write(f"[{presentime}] : {user} donated {string1}\n")
        except Exception as e:
            print("Error : Check your input !!")

    elif(choice == 2):
        try:
            user = input("Enter your full name : ")
            string2 = input("Enter the name of the book you want to borrow : ")
            action2 = Removingbooks(string2)
            action2.removal
            with open("logs.txt","a") as f:
                presentime = datetime.now()
                f.write(f"[{presentime}] : {user} borrowed {string2}\n")
            with open("borrowed_books.txt","a") as f:
                presentime = datetime.now()
                f.write(f"[{presentime}] : {user} borrowed {string2}\n")
        except (ValueError, TypeError):
            print("No this Book is not there in the Library")
    

    elif(choice ==3):
        action3 = SeeingBooks() 
        action3.viewing
    
    elif(choice == 4):
        action4 = Logs()
        print("Choices :-")
        print("(1) Viweing the whole log")
        print("(2) Viewing only the log of Donated books")
        print("(3) Viewing only the log of Borrowed books")
        user_choice = int(input("Enter : "))
        if(user_choice  == 1):
            action4.whole_hist
        elif(user_choice  == 2):
            action4.donating
        elif(user_choice  == 3):
            action4.borrowed_hist

    elif(choice > 4):
        print("PLease enter a valid serial number")

except Exception as e:
    print("Error : Please Check your input !!")