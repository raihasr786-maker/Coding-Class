def Find_Max(x,y,z):
    if (x>y) and (x>z):
        return x
    elif  (y>z) and (y>x):
        return y
    else:
        return z
num1=int(input("Enter first number-> "))
num2=int(input("Enter second number-> "))
num3=int(input("Enter third number-> "))
result_func=Find_Max(num1,num2,num3)
print(result_func)