char=input("Type in a character->  ")
if (ord (char) >= 65 and ord (char) <= 90) or (ord (char) >= 48 and ord (char) <= 57) or (ord (char) >= 97 and ord (char) <= 122):
    print("It is not a special character")
else:
    print("It is a special character")