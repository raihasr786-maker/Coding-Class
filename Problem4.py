def num_status(n):
    if n > 0:
        return "Postive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
num=int(input("Type in a number-> "))
resultfunc=num_status(num)
print(resultfunc)