# append-used to add items at the end of the list
my_list=["Mike","Jane","Alex",1000,200,2000,True,False]
my_list.append("Zac")
print(my_list)

# insert-adds an item at a specified position/index in the list
my_list.insert(1,"Mary")
print(my_list)

# pop-removes an item at a specified index and when not specified ir removes the last one
my_list.pop()
print(my_list)
my_list.pop(3)
print(my_list)

# task1
lst=[10,20,30,['Jane','Mary',[1000,2000,3000]],40,50,60]
# using methods
# add 70 at the end of the list
lst.append(70)
print(lst)

# add 1500 between 1000 and 2000
lst[3][2].insert(1,1500)
print(lst)

# delete 2000
lst[3][2].pop(2)
print(lst)

# sort- used to arrange list items in ascending order but by default
lst1=[1,2,50,10,20,5,2]
lst1.sort()
print(lst1)
lst1.sort(reverse=True)
print(lst1)

lst2=["Mike","Jane","Alex"]
lst2.sort()
print(lst2)
# its case sensitive hence when the 'A' is in small letters the letter in caps starts ie. Jane in this case

lst2=["Mike","Jane","alex"]
lst2.sort()
print(lst2)

# remove= removes a specified element but this one uses the name of the element to basically remove it
lst2.remove("alex")
print(lst2)

# extend- extends a list with another list more like concatenating them
lst2=["Mike","Jane","Alex"]
lst1=[1,2,50,10,20,5,2]
lst2.extend(lst1)
print(lst2)

#=concatenation
lst3=lst1+lst2
print(lst3)

# clear-clears all the data
my_list.clear()
print(my_list)

# in membership
lst2=["Mike","Jane","Alex"]
lst2=("Alex" in lst2)
print(lst2)





