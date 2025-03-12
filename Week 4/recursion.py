# recursion 

def data(n):
    if n==0:
        return 0
    return n + data(n-1)

n = int(input("Enter any number:"))
print("The sum of number you entered form 1 is:", data(n))