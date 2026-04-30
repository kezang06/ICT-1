#Write a recursive function fun(x,y) such that:
#a. if x becomes 0, the function returns of the value of y
# b.Otherwise, the function calls itself:
# i. decreasing x by 1
# ii.adding the current value of x to y
# Eg. When x= 5 and y= 2, the function should compute:
# 2+5+4+3+2+1=17 

def fun1(x,y):
    if x==0:
        return y

    else:
        return fun1(x-1, x+y) 

x= int(input("Enter value of x:"))
y= int(input("Enter value of y:"))

result= fun1(x,y)

print("result:",result)