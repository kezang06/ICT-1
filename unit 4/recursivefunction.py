#Sum of ntaural numbers using recursing
def sum(n):

    if n==1: #base condiiton
        return 1
    
    else: #recursive call
        return n + sum (n-1)
    
n=int(input("Enter a number:"))
print("Sum of numbers from 1 to", n, "is:", sum(n))