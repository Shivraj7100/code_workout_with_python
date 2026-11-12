#1) While loop:

# count = 1 #iterator
# while count <= 5:
#     print("Welcome to python programming")
#     count +=1


#Example:2 # ATM PIN Verification. An ATM keeps asking for your PIN as long as 
# the entered code is incorrect and attempts remain. Once you enter the right PIN, 
# the condition changes and the machine grants access

current_pin = 1234
attempts = 3

while attempts > 0:
    entered_pin = int(input("Enter The Pin:"))

    if entered_pin == current_pin:
        print("welcome to your account")
        break

    else:
        attempts -= 1
        print("Incorrect pin,you have", attempts,"attempts left", "please reenter the pin" )    

        if attempts > 0:
            print("please reenter the correct pin")

        else:
            print("you have exceeded the maximum number of attempts, your account is locked")