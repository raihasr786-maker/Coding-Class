def adding_value(starting,ending):    
    sum=0
    i=starting
    while i <= ending:
        sum=sum+i
        i=i+1
    return sum
def main():
    start=int(input("Type in the starting value-> "))
    end=int(input("Type in the ending value-> "))
    result_func=adding_value(start,end)
    print(f"The sum from {start} to {end} is {result_func}")

if __name__ == "__main__":
    main()