#1. write a program that asks the user for email and password checks if the email is equal to "admin@gmail.com" and the password is equal to "admin123" if it is print "Access granted" otherwise print"Access denied"
email=input("enter email: ")
password=input("enter password: ")
# declare variables to store the data
correct_password="admin123"
correct_email="admin@gmail.com"

if email==correct_email and password==correct_password:
    print("Access granted")
else:
    print("Access denied")

#2. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"

password=input("Enter password:")
# declare a variable to store the password.
correct_password="secret123"

if password== correct_password:
    print("Access granted")
else:
    print("Access denied")

#3. write a program that checks:
# "small" if number <10
# "medium" if 10-50
# "large" if above 50

num=input("Enter number:")
num=int(num)
if num<10:
    print("Small")
elif 10<= num <=50:
    print("Medium")
else:
    print("Large")

#4. Take three inputs from a user, separately. Print the largest of the numbers.
 # Hint: Determine what type of data is taken in as input.
a=(input('Enter first number:'))
a=int(a)
b=(input('Enter second number:'))
b=int(b)
c=(input('Enter third number:'))
c=int(c)
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

 # 5. four inputs from user separately print the largest number
num1=input('Enter first number:')
num1=int(num1)
num2=input('Enter second number:')
num2=int(num2)
num3=input('Enter third number:')
num3=int(num3)
num4=input('Enter fourth number:')
num4=int(num4)
if num1>num2 and num1>num3 and num1>num4:
    print(num1)
elif num2>num1 and num2>num3 and num2>num4:
    print(num2)
elif num3>num1 and num3>num2 and num3>num4:
    print(num3)
else:
    print(num4)

#6. Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”

temp =(input("Enter temperature: "))
temp= float(temp)

if temp > 30:
    print("The temperature is too high")
elif temp > 15 and temp<=30:
    print("Normal temperature")
else:
    print("Cold temperature")

#7. create a program that checks a user's balance 
# "insufficient funds" if <100
# "Moderate balance" if 100-1000
# "high balance" if >1000

balance=input("Enter balance:")
balance=int(balance)

if balance<100:
    print("insufficient funds")
elif 100<= balance <=1000:
    print("moderate balance")
else:
    print("high balance")

#8. Write a Python program that checks if a variable x is between 10 and 20 (inclusive)and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"

x = (input("Enter value of x: "))
x=int(x)
y = (input("Enter value of y: "))
y=int(y)

if 10 <= x <= 20 and y > 100:
    print("Conditions met")
else:
    print("Conditions not met")



    # NB:indentation is key for your code to run..