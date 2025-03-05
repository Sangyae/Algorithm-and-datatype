# Checking if the number is in order or not

# def order(num):
#     return num == sorted(num)

# num_str = (input("Enter any three numbers with space in each numberes: "))

#     if len(num_str) == 3 and order.isdigit():

def is_sorted(numbers):
    return numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True)

# Get user input
num_str = input("Enter three numbers without spaces (e.g., 123 or 321): ")

if len(num_str) == 3 and num_str.isdigit():
    numbers = list(map(int, num_str))
    if is_sorted(numbers):
        print("in order")
    else:
        print("not in order")
else:
    print("Please enter exactly three digits.")
