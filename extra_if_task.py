# 1.
# Write a program that checks login credentials:
# "Access granted" if email = "admin@gmail.com" and password = "Admin@123"
# "Wrong password" if email is correct but password is wrong
# "Email not found" otherwise

email=input("Enter your email: ")
password=input("Enter password: ")

correct_email="admin@gmail.com"
correct_password="Admin@123"

if email==correct_email and password==correct_password:
    print("Access granted")
elif email==correct_email and password !=correct_password:
    print("Wrong password")
else:
    print("Email not found")
# # 2.
# # Create a program that validates an email:
# # "Invalid email" if it does not contain "@" or "."
# # "Gmail account" if it ends with "@gmail.com"
# # "Other email provider" otherwise

email=input("Enter your email: ")

if "@" or "." not in email:
    print("Invalid email")
elif email.endswith("@gmail.com"):
    print("Gmail account")
else:
    print("Other email provider")

# 3.
# Write a program that checks password strength:
# "Weak" if length < 6
# "Moderate" if length 6–10 and contains at least one digit
# "Strong" if length > 10 and contains both digits and uppercase letters

password=("Enter password: ")
if len(password)>=6 and len(password)<=10 and password.isalnum () and password.isupper:
    print("strong")
else:
    print("wrong")

# 4.
# Write a program that checks a password:
# "Invalid" if it does not start with a capital letter
# "Invalid" if it does not end with a number
# "Valid password" otherwise



# 5.
# Write a program that takes a number and checks:

# "Fizz" if divisible by 3
# "Buzz" if divisible by 5
# "FizzBuzz" if divisible by both
# Otherwise print the number

# 6.
# Create a program that takes a score and prints a grade:
# A (≥ 80)
# B (70–79)
# C (60–69)
# D (50–59)
# F (< 50)

# 7.
# Create a program that takes two numbers and prints:
# "Equal" if same
# "First is greater"
# "Second is greater"

# 8.
# Write a program that takes a day number (1–7) and prints:
# Weekday (1–5)
# Weekend (6–7)
# Invalid input otherwise

# 9.
# Create a program that takes a temperature and prints:
# "Freezing" if ≤ 0
# "Cold" if 1–15
# "Warm" if 16–30
# "Hot" if > 30

# 10.
# Create a program that takes a year and prints:
# "Leap year" if divisible by 4
# "Century year" if divisible by 100
# "Common year" otherwise