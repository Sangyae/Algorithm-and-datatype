# counting how many digits the user input
def digits_count(num):
    if num < 0:
        num = num *-1

    if num == 0:
        return 1
    count = 1

    if num >= 10:
        count = 2
    if num >= 100:
        count = 3
    if num >= 1000:
        count = 4
    if num >= 10000:
        count = 5
    if num >= 10000:
        count = 6
    if num >= 100000:
        count = 7
    if num >= 1000000:
        count = 8
    if num >= 100000000:
        count = 9
    if num >= 1000000000:
        count = 10

    return count
num = int(input("Enter any number of digits:"))
print("The number you entered has", digits_count(num),"digits.")

