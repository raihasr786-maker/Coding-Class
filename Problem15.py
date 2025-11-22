def compare_signs(a,b):
    if (a < 0) and (b < 0) or (a > 0) and (b > 0):
        return "Same Sign"
    elif (a < 0) and (b > 0) or (a > 0) and (b < 0):
        return "Different Sign"
    else:
        return "Zero"
def main():
    num1=int(input("Type in a number-> "))
    num2=int(input("Type in a number-> "))
    result_func=compare_signs(num1,num2)
    print(result_func)
if __name__ == "__main__":
    main()