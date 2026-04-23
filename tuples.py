days_of_the_week=('sunday','monday','tuesday','wednesday','thursday','friday','saturday')
print(type(days_of_the_week))

# display sunday
print(days_of_the_week[1])

# display tuesday and wednesday
print(days_of_the_week[2:4])

# display saturday
print(days_of_the_week[-1])

# display thursday to saturday
print(days_of_the_week[4:7])

# convert tuple to list list()
days_of_the_week=list(days_of_the_week)
print(type(days_of_the_week))

# modify
days_of_the_week[2]='Tue'
# convert back to a tuple tuple ()
days_of_the_week=tuple(days_of_the_week)
print(days_of_the_week)

# sunday to Sun

days_of_the_week=list(days_of_the_week)
days_of_the_week[0]='Sun'
print(days_of_the_week)
days_of_the_week=tuple(days_of_the_week)
print(type(days_of_the_week))

# add jan to the tuple
days_of_the_week=list(days_of_the_week)
days_of_the_week.append('Jan')
print(days_of_the_week)
days_of_the_week=tuple(days_of_the_week)

# Tuple methods
# index
# count

# poisition of the data
print(days_of_the_week.index('friday'))
# appearance of value
print(days_of_the_week.count('friday'))


list task on slides

