my_tuple =('Hello',123456) #output: ('Hello', 123456)
print(type(my_tuple)) #output: <class 'tuple'>
print(my_tuple) #output: ('Hello', 123456)
print(my_tuple[0]) #output: 'Hello'
print(my_tuple[-1]) #output: 123456
a, b = my_tuple 
print(b) #output: 123456
new_tup = tuple(a) #output: ('H', 'e', 'l', 'l', 'o')
print(new_tup) #output: ('H', 'e', 'l', 'l', 'o')
concatented_tuple = my_tuple + new_tup
print(concatented_tuple)  #output: ('Hello', 123456, 'H', 'e', 'l', 'l', 'o')
print(concatented_tuple[2:6:1]) #output: ('H', 'e', 'l', 'l')
print(concatented_tuple[::-1]) #output: ('o', 'l', 'l', 'e', 'H', 123456, 'Hello')
del my_tuple #output: NameError: name 'my_tuple' is not defined
print(concatented_tuple[6:1:-4]) #output: ('o', 'H')
n = concatented_tuple[2:7:4] 
print(n[::-1]) #output: ('o', 'H')