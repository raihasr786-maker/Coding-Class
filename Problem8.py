def check_character(char):
    if (ord (char) == 65) or (ord (char) == 69) or (ord (char) == 73) or (ord (char) == 79) or (ord (char) == 85):
        return "It is a vowel"
    else:
        return "It is a Consonant"
character=input("Type in a uppercase letter-> ")
resultfunc=check_character(character)
print(resultfunc)
