# power of 2

def pow_of_two(num):
    if num <= 0:
        return 1
    
    return 2**num

num = int(input("Enter the any integer number to get 2 power: "))
print("The power of 2,",num,"is", pow_of_two(num))