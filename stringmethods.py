text="software DEveloper"
# capitalize-makes the first character uppercase while the rest lowercase
text1=text.capitalize()

print(text1)

text2=text.count('e')
# counts the number of appearance of a specific character in a string

print(text2)

text3=text.lower()
# makes characters lowercase
print(text3)

txt=("           software development        ")
print(len(txt))
text4=txt.strip()
# removes leading and trailing spaces
print(text4)
txt="software development"
# returns the index of the first occurrence of a character
print(txt.find('e'))

print(txt.replace('software','python'))

email='mitchellewanjohi@gmail.com'
split_email=email.split('@')
print(split_email)

text='software developer'
text1=text.split()
print(text1)

# task1
text='    jUnIoR deVeLOper    '
# clean to Junior developer

text=text.strip()
text=text.capitalize()
print(text)

