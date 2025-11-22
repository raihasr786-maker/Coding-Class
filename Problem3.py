def FindMax(x,y,z):
    if (x>y) and (x>z):
        return x
    elif (y>x) and (y>z):
        return y
    else:
        return z
num1=int(input("Type in a number-> "))
num2=int(input("Type in a number-> "))
num3=int(input("Type in a number-> "))
resultfunc=FindMax(num1,num2,num3)
print(resultfunc)