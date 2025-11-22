def calculate_grade():
    marks=int(input("Enter the student score-> ")) 
    if marks >= 50:
        print("Pass!!")
        if marks >= 90:
            print("Exellent")
        elif marks >= 65:
            print("Good")
        else:
            print("Needs improvement")
    else:
        print("Fail!")
calculate_grade()
calculate_grade()
calculate_grade()