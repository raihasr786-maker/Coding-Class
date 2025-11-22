a=int(input("Enter the length->  "))
b=int(input("Enter the length->  "))
c=int(input("Enter the length->  "))
if (a+c>b) and (b+c>a) and (a+b>c):
    print("It is a triangle")
else:
    print("It is not a triangle")