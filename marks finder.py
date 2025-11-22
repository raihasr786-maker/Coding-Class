total_marks_in_Math=int(input("Enter total marks in Math->"))
total_marks_in_Science=int(input("Enter total marks in Science->"))
total_marks_in_English=int(input("Enter total marks in English->"))
total_marks_in_History=int(input("Enter total marks in History->"))
total_marks_in_Sports=int(input("Enter total marks in Sports->"))

Obtained_marks_in_Math=float(input("Enter Obtained marks in Math->"))
Obtained_marks_in_Science=float(input("Enter Obtained marks in Science->"))
Obtained_marks_in_English=float(input("Enter Obtained marks in English->"))
Obtained_marks_in_History=float(input("Enter Obtained marks in History->"))
Obtained_marks_in_Sports=float(input("Enter Obtained marks in Sports->"))

Percentage_in_Math=(Obtained_marks_in_Math/total_marks_in_Math)*100
Percentage_in_Science=(Obtained_marks_in_Science/total_marks_in_Science)*100
Percentage_in_English=(Obtained_marks_in_English/total_marks_in_English)*100
Percentage_in_History=(Obtained_marks_in_History/total_marks_in_History)*100
Percentage_in_Sports=(Obtained_marks_in_Sports/total_marks_in_Sports)*100


total_marks=total_marks_in_English+total_marks_in_History+total_marks_in_Math+total_marks_in_Science+total_marks_in_Sports
obtained_marks=Obtained_marks_in_English+Obtained_marks_in_History+Obtained_marks_in_Math+Obtained_marks_in_Science+Obtained_marks_in_Sports
print(f"The percentage in Math is {Percentage_in_Math}%")
print(f"The percentage in Science is {Percentage_in_Science}%")
print(f"The percentage in English is {Percentage_in_English}%")
print(f"The percentage in History is {Percentage_in_History}%")
print(f"The percentage in Sports is {Percentage_in_Sports}%")
print(f"THe maximum points you could obtained is {total_marks}")
print(f"The point you have obtained is {obtained_marks}")

