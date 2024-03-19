#Netflix type system demo - FakeFlix
import csv
import sys

def main():
   menu()


def menu():
    print("************Welcome to FakeFlix Demo**************")
    print()

    flag = True
    while flag:
        choice = input("""
                      A: Please Register
                      B: Login
                      Q: Logout

                      Please enter your choice: """)

 
        if choice == "A" or choice =="a":
            register()
        elif choice == "B" or choice =="b":
            login()
        elif choice=="Q" or choice=="q":
            flag = False
            sys.exit
        else:
            print("You must only select either A or B")
            print("Please try again")
            menu()

def register():
   print("register")
   pass
    
def login():
   print("login")
   pass
    
#the program is initiated, so to speak, here
main()