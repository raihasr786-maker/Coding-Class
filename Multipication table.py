num=int(input("Type in a number-> "))
amount_of_numbers=int(input("How many numbers do you need?-> "))
counter=0
while counter <= amount_of_numbers:
    print(f"{num}*{counter} == {num*counter}")
    counter=counter+1