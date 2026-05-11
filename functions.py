# def hello():
#     print("Hello Alex")

# hello()

# def triangle_area():
#     base=10
#     height=20
#     area=0.5*base*height
#     print(area)

# triangle_area()

# # area of circle
# def circle_area():
#     pi=3.142
#     radius=21
#     area=pi*radius**2
#     print(area)

# circle_area()

# # reusing name

# def hello(name):
#     print(f"Hello {name}")

# hello("Mishi")
# hello("Hailey")

# # area of triangle-reused

def triangle_area(base,height):
    area=0.5*base*height
    return area



triangle1=triangle_area(10,20)
print(triangle1)
triangle2=triangle_area(20,50)
print(triangle2)

# # area of circle-reused

# def circle_area(radius):
#     pi=3.142
#     area=pi*radius**2
#     return area

# circle1=circle_area(21)
# print(circle1)
# circle2=circle_area(14)
# print(circle2)
# # create a function that calculates the area of a rectangle and reuse it

# def rectangle_area(length,width):
#     area=length*width
#     return area

# rectange1=rectangle_area(12,3)
# print(rectange1)
# rectange2=rectangle_area(5,8)
# print(rectange2)
# rectange3=rectangle_area(6,8)
# print(rectange3)

# #  2. Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
# #  Hint: how does an even / odd number react differently when divided by 2?

# def check_number(num):

#     if num %2==0:
#      res= "even"
#     else:
#      res= "odd"
#     return res

# num1=int(input("Enter number: "))
# num1=check_number(12)
# print(num1)

# 10. Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

def total_stock(stock):
    total=0
    for i in stock:
        quantity=i[2]
        quantity=int(i[2])
        total=total+quantity

    return total

prods=[['omo','30kshs','300'], ['milk','50kshs','200'],['bread','45kshs','359'],['coffee','5kshs','79']]

tot=total_stock(prods)
print(tot)

# 12. Write a program that prints the largest of 4 inputs taken as input from a user.

def largest_number(num1,num2,num3,num4):

    if num1>num2 and num1>num3 and num1>num4:
        largest=num1
    elif num2>num1 and num2>num3 and num2>num4:
        largest=num2
    elif num3>num1 and num3>num2 and num3>num4:
        largest=num3
    else:
        largest=num4

    return largest

input1=input("Enter number: ")
input2=input("Enter number: ")
input3=input("Enter number: ")
input4=input("Enter number: ")

check1=(largest_number(input1,input2,input3,input4))
print(check1)


# 4. Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
#  Hint: Check if it contains an “@” symbol and “.” symbol.

def enter_email(email):

    if "@"  in email and "." in email:
        res="Valid email."
    else:
        res="Invalid email."              
    return res

email1=input("Enter your email: ")

cor=enter_email(email1)
print(cor)


# 7. Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40

def grading(marks):

    if marks>=0 and marks<=100:
        if marks>79:
            grade="A"
        elif marks<79 and marks>=60:
            grade="B"
        elif marks<60 and marks>=49:
            grade="C"
        elif marks<49 and marks>=40:
            grade="D"
        elif marks:
            grade="E"
    else:
        grade="Invalid"
    return grade
        
marks1=int(input("Enter student marks: "))

mar=grading(marks1)
print(mar)