#The volume of the sphere with radius r si (4/3)*pie * r**2.
#what is the volume of sophere with radius 5
#nake sure that that the program enters the radius from the keyboard and provide the answer in 2 decimal places
radius = float(input('enter the radius'))
pie = float(22/7)
volume = (4/3)*pie*(radius**2)
print(f"the volume of the sphere is {volume:.2f}")


#Question 2
#create a program to calculate the area of traingle (1/2*base*height) .
#base and height should be entered using the key board
base = float(input("Enter the the base of the triangle:"))
height = float(input("Enter the the height of the triangle:"))
area= (1/2)*base*height
print(f"the area of the triangle is{area} ")


# Questio 3
# witi has asked you to automate a simple grading system.
#As a python student , write a programe using to display the grades 
#the student will de recieving based  on the mark scored in subject.
# The grades are :
#90% - 100% grade is A 
#80% - 89% grade is B 
#70% - 79%  grade is C
#60% - 69%   grade is D
#50% - 59% grade is E
# < 50% fail

score = int(input("Enter the student's score:\t"))

if 90 <= score <= 100:
   print("Grade is A")
elif 80 <= score<= 89:
   print("Grade is B")
elif 70 <= score<= 79:
   print("Grade is C")
elif 60 <= score<= 69:
   print("Grade is D")
elif 50<= score<= 59:
     print("Grade is E")
else:
    print("fail")



#Question 4
##  WITI Academy is proposing a Sacco to help students save their money. 
#  Design a platform that will do the following.
#  Welcome to, WITIAcademy Sacco.
#  1. Deposit Money
#  2. Withdraw Money
#  3. Check Balance
#  Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#  If the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
#  If the student selects 3, the account balance should be displayed
balance = 0

print("Welcome to WITIAcademy Sacco")
print("\nPlease choose an option:")
print("1. Deposit Money")
print("2. Withdraw Money")
print("3. Check Balance")


choice = input("Enter your choice (1/2/3): ")

if choice == '1':  
    amount = float(input("Enter amount to deposit: "))
    if amount >= 1000:
        balance += amount
        print(f"Successfully deposited {amount}. New balance is {balance}.")
    else:
        print("Minimum deposit amount is 1000.")

elif choice == '2': 
    amount = float(input("Enter amount to withdraw: "))
    if amount >= 500:
        if balance >= amount:
            balance -= amount
            print(f"Successfully withdrew {amount}. New balance is {balance}.")
        else:
            print("Insufficient balance.")
    else:
        print("Minimum withdrawal amount is 500.")

elif choice == '3':  # Check Balance
    print(f"Your current balance is {balance}.")

else:
    print("Invalid choice.")

