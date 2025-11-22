def sum(x,y):
    result=x+y
    return result
def diffrence(x,y):
    result=x-y
    return result
def product(x,y):
    result=x*y
    return result
def quotient(x,y):
    result=x/y
    return result
def calculator(op,x,y):
    if op == "+":
        return sum(x,y)
    elif op == "-":
        return diffrence(x,y)
    elif op == "*":
        return product(x,y)
    elif op == "/":
        return quotient(x,y)
    else:
        return False
def main():
    num1=int(input("Type in a number-> "))
    num2=int(input("Type in a number-> "))
    operation=input("Type in the operation-> ")
    result_func=calculator(operation,num1,num2)
    print(result_func)
if __name__ == "__main__":
    main()