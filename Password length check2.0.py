password=input("Enter a password-> ")
if len(password) >= 8 and len(password) <= 16:
    print("It is a valid password")
else:
    print("It is not a valid password")