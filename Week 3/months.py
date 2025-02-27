# user input and give output as months

def month_to_days(month):
    if month in {1,3,5,7,8,10,12}:
        return "31 days"
    elif month in {4,6,9,11}: #for April, june, september, November
        return " 30 days"
    elif month ==2:             # for Feburary
        return "28 or 29 days"
    else:
        return "You input the wrong input!"
    
month = int(input("Enter numbers from 1-12:"))
print("This month has ", month_to_days(month), "days.")
