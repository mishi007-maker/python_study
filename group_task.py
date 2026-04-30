# (question 1, group1)
# A bank wants to improve its ATM service. Create a program that stores a customer’s name and account balance, then allows them to request a withdrawal. If the amount requested is greater than the available balance, the transaction should fail. If successful, deduct the amount together with a transaction fee of KES 30 and display the new balance.

customer_name=input("Enter your name: ")
account_balance=100000
amount_requested=input("Enter amount: ")
amount_requested=int(amount_requested)
transaction_fee=30

if amount_requested>account_balance:
    res=f"Hello {customer_name}, Transaction failed Insufficient funds to withdraw {amount_requested} your balance is {account_balance}"
else:
    account_balance=account_balance-(amount_requested+transaction_fee)
    res=f"Hello {customer_name},{amount_requested} withdrawn successfully.New balance {account_balance}"

    print(res)


# (question 2, group1)
# A trainer entered marks for five subjects and needs help analyzing student performance. Create a program that stores the marks in a list, calculates the average, awards grade A for averages of 70 and above, grade B for averages of 50 to 69, and grade C for anything below 50. If any subject score is below 40, display a message showing the student must retake that subject.
marks=[20,60.50,100,60]
average=sum(marks)/len(marks)

if average>=70:
    grade="A"
elif average<70 and average>=50:
    grade="B"
elif average<50 and average>=40:
    grade="c"
else:
   grade="Retake the subject"

   print(grade)


# (Q3, group1)
# A supermarket manager needs help checking stock levels. Create a program that stores product names and quantities in a dictionary, identifies items that are completely out of stock, and also shows products with quantities below five units that need urgent restocking.

# question4=loops

# (Q1 group 4)
# A school wants to stop students with pending balances from sitting exams. Create a program that checks a student’s fee balance. If the balance is greater than zero, deny access to the exam card. Otherwise allow printing.
student_name=input("Enter your name: ")
balance=float(input("Enter student fee balance: "))
if balance>0:
    res=f"Hi {student_name} Access denied, your balance is {balance}"
else:
    res=f"Hi {student_name} Access granted"

    print(res)


# Q2 (group 4)
# A parking company wants to automate entry control. Build a program that stores the total parking spaces and occupied spaces, then calculates available slots. If the lot is full, deny new entry.

total_spaces=input("Enter total parking spaces:")
total_spaces=int(total_spaces)
occupied_spaces=input("Enter total occupied spaces:")
occupied_spaces=int(occupied_spaces)

Available_spaces=total_spaces-occupied_spaces

if Available_spaces>0:
    Available_spaces-=1
    value=f"Entry allowed {Available_spaces} spaces available."
else:
    value=f"Entry denied {Available_spaces} available spaces."

    print(value)

# Q3 , group 4
# A mobile network provider wants to warn customers when internet bundles are low. Build a program that checks remaining data in MB. If below 100MB, warn the user. If zero, block browsing.

data=input("Enter Remaining Data")
data=float(data)

if data==0:
    res="block browsing"
elif data<100:
    res=f"Your data balance is {data}MB,below 100"
else:
    res=f"You have {data}MB"

    print(res)

# Q4
# A retail shop wants to identify wholesale customers. Create a system that checks how many items a customer has bought. If items are more than five, reward points should be given.

items=int(input("enter number of items"))
wholesale_threshold=5

if items>5:
    reward_points=items/wholesale_threshold
    val=f"You have bought {items} items you have earned {reward_points} reward points"
else:
    remaining=wholesale_threshold-items
    val=f"You have bought {items} items add {remaining} more than to earn points."

    print(val)



   