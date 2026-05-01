name = input("Enter your name: ")
greet = lambda x: print("Hello", x)
greet(name)

#use cases of lambda function
#1.condition checking
even_Odd = lambda x: "Even" if x%2 == 0 else "Odd"
num = int(input("Enter a number: "))
print(even_Odd(num))

#2.Return Multiple results
arith = lambda x, y: (x+y, x-y, x*y, x/y)
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
print(arith(num1, num2))

#3. filter()
mylist = [1, 2, 3, 4, 5, 6]
even = filter(lambda x:  x % 2 == 0, mylist)
print(list(even))
 
#4. map()
mylist = [1,2,3,4]
double = map(lambda x: x * 2, mylist)
mynewlist = (list(double)) #converting double into mynewlist
print(mynewlist)
division = map(lambda x: x // 2, mynewlist)
print(list(division))

#5. reduce()
from functools import reduce
mylist = [1,2,3,4]
mul = reduce(lambda x, y: x*y, mylist)
print(mul)

