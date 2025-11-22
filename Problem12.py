def day_of_week(x):
    if x == 1:
        return "Sunday"
    elif x == 2:
        return "Monday"
    elif x == 3:
        return "Tuesday"
    elif x == 4:
        return "Wednesday"
    elif x == 5:
        return "Thursday"
    elif x == 6:
        return "Friday"
    elif x == 7:
        return "Saturday"
    else:
        return "It is not a day"    
def main():
    day=int(input("Type in a number that repersents the day-> "))
    result_func=day_of_week(day)
    print(result_func)
if __name__ == "__main__":
    main()

