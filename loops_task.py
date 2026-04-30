# Write a program that displays a numbers 1 to 50 inside a list.

numbers=list(range(1,51))
print(numbers)

# From 1 above display the ones divisible by 7 or 5 inside a list.
divisible=[]

for i in numbers:
    if i%7==0 or i%5==0:
        divisible.append(i)
        
print(divisible)

# # Find sum and average of values in the range between 10 to 40 without tusing

total = 0     
count = 0     

for i in range(10, 41):  
    total = total + i     
    count = count + 1    

average = total / count  

print("Sum:", total)
print("Average:", average)

# Put in a list the first 10 odd numbers between 10 to 50.

odds = []
for i in range(10, 51):  
    if i % 2 != 0:        
        odds.append(i) 
    if len(odds) == 10:   
        break

print("First 10 odd numbers:", odds)


# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
count = 0
for i in range(1, 51):
    if i % 2 == 0:
        count += 1
print("Number of even numbers between 1 and 50:", count)

# ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
# Display the total quantity of the 3 above.
ls1 = [("Jay", '20'), ("Mo", '30'), ("Mya", '32'),('xyz','100')]
total_quantity=0
for i in ls1:
    quantity=int(i[1])
    total_quantity=total_quantity+quantity
print(total_quantity)