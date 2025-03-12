# Doing factorial only

def fact(num):
    if num <= 1:
        return 1
    return num * fact(num-1)

num = int(input("Enter any number:"))
print("The sum of number you entered form 1 is:", fact(num))