my_set = {1, 2, 3, "Hello", 3.14, 1, 2, False} #duplicate values will be removed in a set
print(type(my_set)) #data type of my_set is set
print(my_set) #output: {False, 1, 2, 3, 'Hello', 3.14} #Note: The order may vary
# my_set[0] = "Start" #This will raise an error because sets are unordered and do not support indexing.
my_set.add("World") 
print(my_set) #output: {False, 1, 2, 3, 'Hello', 3.14, 'World'}
my_second_set = {3, 4, 5}
union_set = my_set.union(my_second_set) 
print(union_set) #output: {False, 1, 2, 3, 'Hello', 3.14, 'World', 4, 5} #Note: The order may vary
intersection_set = my_set.intersection(my_second_set)
print(intersection_set) #output: {3}
difference_set = my_set.difference(my_second_set)
print(difference_set) #output: {False, 1, 2, 'Hello', 3.14, 'World'} #Note: The order may vary
my_set.clear()
print(my_set) #output: set() #my_set is now empty