def absolute_value(num):
    if num >= 0:
        return num
    else:
        return (num*-1)
num1=int(input("Type in a number-> "))
result_func=absolute_value(num1)
print(result_func)