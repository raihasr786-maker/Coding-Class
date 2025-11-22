def compare_strings(s1,s2):
    if len(s1)==len(s2):
        return "Equal"
    elif len(s1)<len(s2):
        return "Shorter"
    if len(s1)>len(s2):
        return "Longer"
string1=input("Type in a string-> ")
string2=input("Type in a string-> ")
resultfunc=compare_strings(string1,string2)
print(resultfunc)