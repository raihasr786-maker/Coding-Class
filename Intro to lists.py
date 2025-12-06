def input_print_names():
    names = []
    for i in range(5):
        name=input("Type ina a name-> ")
        names.append(name)
    return names

def print_names(names):
    for i in range(len(names)):
        print(names[i])

def report_card(student_name):
    print(f"{student_name} is passed")

def main():
    names_list=input_print_names()
    print_names(names_list)
    report_card(names_list[2])

if __name__ == "__main__":
    main()