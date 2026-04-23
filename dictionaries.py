my_dict={
    "Name":"Mitchelle",
    "Gender":"Female",
    "Age":"18",
    "City":"Kiambu",
    "location":{"Postal_Code":"00100","Town":"Kiambu"}

}
print(my_dict)
print(type(my_dict))

# accessing values in a dictionary we use keys
print(my_dict["Age"])
print(my_dict["City"])

# update an existing property

my_dict["City"]="Nairobi"
print(my_dict)

# to add a new key
my_dict["age"]=21
print(my_dict)

# to add a new property
my_dict["Occupation"]="Software Development"
print(my_dict)

# dictionary methods

# .pop()
# used to remove a property with a key given out(specific item)
# .popitem()
# used to remove the last added item(ignore)

my_dict.pop('age')
print(my_dict)

my_dict.popitem()
print(my_dict)


