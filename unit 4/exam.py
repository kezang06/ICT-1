#Write a function check_even_odd(num) that:
#Returns “Even” if number is even
#Returns “Odd” otherwise

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
number = int(input("Enter a number: "))
result = check_even_odd(number)
print("The number is:", result)