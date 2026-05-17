#Fcatorial of a number using recursing
def fact(n):

#Base condition
    if n==0:
        return 1
    
    #Recusive call
    else:
        return n * fact(n-1)
    
print("Factorial of 5:", fact(5))