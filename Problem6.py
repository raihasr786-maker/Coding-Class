def leap_year(year):
    if year % 4 == 0:
        return "True"
    else:
        return "False"
currentyear=int(input("Type in a year-> "))
resultfunc=leap_year(currentyear)
print(resultfunc)