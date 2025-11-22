def triangle_type(a,b,c):
    if a==c and a==b:
        return "It is a equalateral triangle"
    elif a == b or a == b or c==a:
        return"It is a isoscles triangle"
    else:
        return"It is a scalene triangle"    
side1=int(input("Type in a number-> "))
side2=int(input("Type in a number-> "))
side3=int(input("Type in a number-> "))
resultfunc=triangle_type(side1,side2,side3)
print(resultfunc)