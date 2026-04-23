# 1. numbers = (10, 20, 30, 40, 50)Add 60 to the end,Replace 30 with 35.
numbers=(10,20,30,40,50)
numbers=list(numbers)
numbers.append(60)
numbers[2]=35
print(numbers)
numbers=tuple(numbers)
print(type(numbers))

# 2. values = (15, 5, 30, 25, 10) arrange the elements in ascending order.
values = (15, 5, 30, 25, 10)
numbers=list(numbers)
numbers.sort()
print(numbers)
numbers=tuple(numbers)
print(type(numbers))

# 3. fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
# Count occurrences of "banana",Remove all occurrences of "banana".
fruits=("apple", "banana", "cherry", "banana", "mango", "banana")
print(fruits.count('banana'))
fruits=list(fruits)
fruits.pop(1)
fruits.pop(2)
fruits.pop(3)
print(fruits)
fruits=tuple(fruits)

# 4. names = ("Alice","Bob","Charlie","David") Reverse the order of elements using sort method.
names = ("Alice","Bob","Charlie","David")
names=list(names)
names.sort(reverse=True)
print(names)
names=tuple(names)
print(type(names))

# 5. colors = ("red", "blue", "green") add "yellow" at index 1,Extend with ["purple", "orange"]
colors = ("red", "blue", "green")
colors=list(colors)
colors.insert(1,"yellow")
print(colors)
colors2=("purple", "orange")
colors.extend(colors2)
print(colors)