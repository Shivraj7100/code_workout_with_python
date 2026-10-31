#Basics of object oriented programming
# class = it is blueprint of class
# object = It is a instance of a class
# def __init__ = it is a constructor of class
# def __init__(self, name, age): = it is a constructor of class which takes two parameters name and age self is a referance to a curreent instance of class
# constructor is a special method which is automatically called when current instace of class is created
# for example: i have defined some data inside one method and that mehod data is print when i create object of class
class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
        user_input = input("""
        Welcome to ATM
        Please choose your option
        1. Enter 1 to check balance
        2. Enter 2 to withdraw money
        3. Enter 3 to deposit money
        4. Enter 4 to change pin
        5. Enter 5 to exit
        """)
        if user_input == "1":
            print(f"Your balance is {self.balance}")

        elif user_input == "2":
            print(f"Your withdrawl money is {self.withdrawl_money()}")

        elif user_input == "3":
            print("Your deposit money is ")

        elif user_input == "4":
            print("Your pin is changed")

        elif user_input == "5":
            print("Thank you for using our ATM")


    def create_pin(self):
        self.pin = input("Enter the pin:")
        print("pin created successfully")

    def deposit_money(self):
        temp = input ("Enter your pin:")
        if temp == self.pin:
            amount = int (input("Enter the amount you want to deposit: "))
            self.balance = self.balance + amount
            print("Deposit successful")
        else:
            print("Invalid pin")
    

    # def withdrawl_money(self):
    #     withdrawl_amount = int(input("Enter the amount you want to withdraw: "))
    #     if withdrawl_amount > self.balance:
    #         print("Insufficient balance")
    #     else:
    #         self.balance -= withdrawl_amount
    #         return withdrawl_amount

    # def deposit_money(self):
    #     deposit_amount = int(input("Enter the amount you want to deposit: "))
    #     self.balance += deposit_amount
    #     return deposit_amount

    # def change_pin(self):
    #     new_pin = input("Enter your new pin: ")
    #     self.pin = new_pin
    #     print("Your pin is changed successfully")

    
