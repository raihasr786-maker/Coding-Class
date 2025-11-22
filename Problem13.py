def find_quadrant(x,y):
    if x > 0 and y > 0:
        return "I" 
    elif x < 0 and y > 0:
        return "II" 
    elif x < 0 and y < 0:
        return "III" 
    elif x > 0 and y < 0:
        return "IV" 
    else:
        return "orgin"
def main():
    run=int(input("Type in a x coordinate-> "))
    rise=int(input("Type in a y coordinate-> "))
    result_func=find_quadrant(run,rise)
    print(result_func)
if __name__ == "__main__":
    main()