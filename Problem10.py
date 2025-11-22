def check_case(char):
    if ord (char) >= 65 and ord (char) <= 90:
        return"It is an uppercase letter."
    if ord (char) >= 97 and ord (char) <= 122:
        return"It is an lowercase letter."
    else:
        return"It is not a letter."
character=input("Type in a letter-> ")
resultfunc=check_case(character)
print(resultfunc)