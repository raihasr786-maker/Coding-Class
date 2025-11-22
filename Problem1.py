def even_check(x):
    result= x % 2 == 0
    return result
num=int(input("Enter a number-> "))
if even_check(num) == True:
    print("Even")
else:
    print("Odd")