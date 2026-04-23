# the condition returns true
if 20>10:
    print('20 is greater')
else:
    print('20 is less')   
# the condition returns false
if 50<30:
    print('50 is greater')

# check if someone is eligible to vote
age=17
if age>=18:
    print('Eligible to vote')
else:
    print('Not eligible')

# check if temperature is greater than 30 print too hot otherwise normal temperature

temp=25
if temp>30:
    print('too hot')
else:
    print('normal temperature')

marks=60
if marks>=80:
    print('grade A')
elif marks>=70 and marks<80:
    print('grade B')
elif marks>=60 and marks<70:
    print('grade C')
elif marks>=50 and marks<60:
    print('grade D')
else:
    print('grade E')


# check if temperature is greater than 30 print too hot, if temperature is above 15 and less than 30 normal temperature , otherwise too cold.
temp=29
other=30
if temp>30:
    print('too hot')
elif temp>15 and temp<30:
    print('normal temperature')
else:
    print('too cold')



