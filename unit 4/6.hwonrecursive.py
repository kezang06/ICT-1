def pattern(n):
    if n == 0:
        return
    
    pattern(n - 1)   # call with smaller value
    
    print("*" * n)  # print after recursion (increasing)

n = int(input("Enter a number: "))

pattern(n)