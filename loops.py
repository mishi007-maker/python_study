numbers=list(range(10,101))
even_numbers=[]


for i in numbers:
    if i%2==0:
        even_numbers.append(i)

print(even_numbers)


# display numbers divisible by 3 and 7 from numbers to 100

numbers=list(range(1,101))
even_numbers=[]

for i in numbers:
    if i%3==0 and i%7==0:
        even_numbers.append(i)

print(even_numbers)


# pin structure

attempts=3
attempts=list(range(1,4))

for i in attempts:
	pin=input('Enter pin:')
	correct_pin='1234'
	if pin==correct_pin:
		print("Welcome")
		break
	else:
		remaining_tries=tries-i
		if remaining_tries>0:
			print(f'incorrect pin try again {remaining_tries} attempts remaining')
		else:
			print("account Blocked")