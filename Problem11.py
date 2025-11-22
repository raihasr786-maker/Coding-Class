def FindMax(w,x,y,z):
    if (x>y) and (x>z) and (x>w):
        return x
    elif (y>x) and (y>z) and (y>w):
        return y
    elif (z>x) and (z>y) and (z>w):
        return z
    else:
        return w
num1=int(input("Type in a number-> "))
num2=int(input("Type in a number-> "))
num3=int(input("Type in a number-> "))
num4=int(input("Type in a number-> "))
resultfunc=FindMax(num1,num2,num3,num4)
print(resultfunc)