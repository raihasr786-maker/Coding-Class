def calculate_grade(score):
    if score >= 90:
        return "A"
    elif (score >= 80) and (score <= 89):
        return "B"
    elif (score >= 70) and (score <= 79):
        return "C"
    elif (score >= 60) and (score <= 69):
        return "D"
    else:
        return "Fail"
grade=int(input("Type in your grade-> "))
resultfunc=calculate_grade(grade)
print(resultfunc)