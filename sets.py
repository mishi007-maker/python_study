days_of_the_week={"Mon","Tue","Wed","Thur","Fri","Sat","Sun","Mon","Mon","Sun"}
print(days_of_the_week)

# =>set function()-converts data structures into sets to achieve unique items..to remove duplicates
# set methods
days_of_the_week.remove('Sun')
print(days_of_the_week)
days_of_the_week.remove("Fri")
print(days_of_the_week)

days_of_the_week.add('Sun')
print(days_of_the_week)
days_of_the_week.add("Fri")
print(days_of_the_week)