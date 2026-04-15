# Questions create a new file
# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
temp=56.8926
print(type(temp))
print(round(temp))
temp=int(temp)
print(type(temp))

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89 
temp=56.8926
temp2=round(temp,2)
print(temp2)

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893 
temp=56.8926
temp2=round(temp,3)
print(temp2)

# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
temp=56.8926
temp=str(temp)
print(type(temp))
temp=temp[3]+"."+temp[4:8]
print(temp)
temp=float(temp)
print(type(temp))
print(temp)




