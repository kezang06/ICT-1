#Write a program using functions to :
#a.Input marks of 3 subjects
#b.Create a function calculate_total(m1,m2,m3)
#c.Create another function calculate_average(total)
#Prints the result of the student according to the average(if average >=50:return Pass, else return fail)


# Function to calculate total
def calculate_total(m1, m2, m3):
    return m1 + m2 + m3

# Function to calculate average
def calculate_average(total):
    return total / 3

# Input marks
m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))

# Function calls
total = calculate_total(m1, m2, m3)
average = calculate_average(total)

# Display results
print("Total marks:", total)
print("Average marks:", average)

# Pass/Fail condition
if average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")