# 1. clean up the following variable to give the clean version in lower case. using inbuit functions in the str class
# name=JOHn to john
name="JOHn  ."
name=name.replace(".","")
name=name.strip()
name=name.lower()
print(name)

# 2. slice the below string to get you the resulting sentence
sentence="The Dog Breed is German Shepherd"
print(sentence.find('n'))
print(sentence[8:23])

# b.

sentence_two="Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:30])

# 3. split using the semicolon and print length of outcome
split="The lazy dog; ran so fast; it hit the wall."
split1=split.split(';')
print(split1)
print(len(split1))

# 4.clean up
first_name=" Joh.n"
last_name="Do,e"

first_name=first_name.strip()
first_name=first_name.replace(".",'')
print(first_name)

last_name=last_name.strip()
last_name=last_name.replace(",","")
print(last_name)

full_name=first_name+" "+last_name
print(full_name)


# 5. manipulate to EWC

r='["E", "W", "C"]'
r=r.replace(",","")
r=r.replace('"',"")
r=r.replace("[","")
r=r.replace("]","")
r=r.replace(" ","")
print(r)

            