# area of a rectrangle
l = float(input("Enter length of a rectangle: "))
w = float(input("Enter width of a rectangle: "))
area = (l * w)
print(area)
 
#find the largest of two number
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
if (num1 > num2):
    print("num1 is greater")
if (num2 > num1):
    print("num2 is greater")
else:
    print("Both numbers are equal")

#write a pseudocode to check if the user has entered any input
# if the input is blank, display an error message
user_input = input("enter your CID no. : ")
if user_input == str(input("")):
    print("Error: Input cannot be blank")
else:
    print("Input received successfully, thank you")
