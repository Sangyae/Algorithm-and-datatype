# Doing factorial only

def fact(num):
    if type(num) != int:
        return None
    if num < 0:
        return None
    if num <= 0:
        return 1
    return num * fact(num-1)

num =(input("Enter any number:"))
print("The factorail of number",num, "is:", fact(num))