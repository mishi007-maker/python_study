# 1. Write a program that prompts the user to enter the base and height of a triangle and returns its area.
# base=int(input("Enter the base:"))
# height=int(input("Enter the height:"))
# area=0.5*base*height
# print("Area:",area)

# # 2. Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
# #  Hint: how does an even / odd number react differently when divided by 2?

# number=int(input("Enter number: "))

# if number %2==0:
#     res=f"{number} is even"
# else:
#     res=f"{number} is odd"
# print(res)

# # Extras:
# # If the number is a multiple of 4, print out “divisible by 4”.

# number=int(input("Enter number: "))

# if number %4==0:
#     res=f"{number} is divisible by 4"
# else:
#     res=f"{number} is not divisible by 4"

# print(res) 

# # 3. Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# # e.g if a user enters “0712345678”, the program should display “+254712345678”
# # e.g if a user enters “0112345678”, the program should display “+254112345678”
# # e.g if a user enters “712345678”, the program should display “+254712345678”

# phone = input("Enter phone number: ")

# if phone.startswith("+254") and len(phone) == 13:  
#     res=(phone)
# elif phone.startswith("254") and len(phone) == 12:  
#     res=("+254" + phone[3:])
# elif phone.startswith("0") and len(phone) == 10:   
#     res=("+254" + phone[1:])
# elif (phone.startswith("7") or phone.startswith("1")) and len(phone) == 9: 
#     res=("+254" + phone)
# else:
#     res=("Invalid number")
# print(res)

# # 4. Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# # Hint: Check if it contains an “@” symbol and “.” symbol.

# email=input("Enter your email: ")

# if "@"  in email and "." in email:
#     print("Valid email.")
# else:
#     print("Invalid email.")                   

# # 5.Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
# # The goal of this exercise is to think about some internals that programs normally take care of for us. 

# def largest_number(user1,user2,user3):

#     if user1>user2 and user1>user3:
#         largest=user1
#     elif user2>user1 and user2>user3:
#         largest=user2
#     else:
#         largest=user3

#     return largest

# input1=("Enter number: ")
# input2=("Enter number: ")
# input3=("Enter number: ")

# check1=largest_number(input1,input2,input3)
# print(check1)

# # 6.Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
# # attempts=[1,2,3,4]

# for i in attempts:
# 	password=input('Enter password:')
# 	correct_password='admin@123'
# 	if password==correct_password:
# 		print("Access Granted")
# 		break
# 	else:
# 		remaining_attempts=len(attempts)-i
# 		if remaining_attempts>0:
# 			print(f'incorrect password...try again {remaining_attempts} attempts remaining')
# 		else:
# 			print(f"incorrect password...try again {remaining_attempts} attempts remaining..account Blocked")

# # 7. Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# # A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40

# marks=int(input("Enter student marks: "))
# if marks<=100:
#     if marks>79:
#         grade="A"
#     elif marks<79 and marks>=60:
#         grade="B"
#     elif marks<60 and marks>=49:
#         grade="C"
#     elif marks<49 and marks>=40:
#         grade="D"
#     elif marks:
#         grade="E"
# else:
#     grade="Invalid"

# print(grade)

# # 8.Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# # For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.

# speed = int(input("Enter car speed: "))
# limit = 70

# if speed <= limit:
#     print("Ok")
# else:
#     points = (speed - limit) / 5
#     if points > 12:
#         print("License suspended")
#     else:
#         print(f"Points: {points}")

# # 9.Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# # Example If rows is 5, it should print the following:
# # *
# # **
# # ***
# # ****
# # *****.....

# rows=int(input("Enter number: "))
# for i in range(1, rows + 1):
#     print("*" * i)

# 10. Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

prods = [['omo','30kshs','300'], ['milk','50kshs','200'],['bread','45kshs','359'], ['coffee','5kshs','79']]

for i in int(range(prods[2])):
     print(i)
     





