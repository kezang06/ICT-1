# 1. Taking Inputs
name = input("Enter Student Name: ")
marks = []
for i in range(1, 5):
    m = float(input(f"Enter marks for Module {i} (0-100): "))
    marks.append(m)

attendance = float(input("Enter Attendance (%): "))

# 2. Calculations
average = sum(marks) / len(marks)

# Determine Pass or Fail (Assuming 50 is the passing mark)
status = "Pass" if average >= 50 else "Fail"

# Determine Grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Determine Eligibility for Reward (e.g., Average > 90 and Attendance > 90%)
eligible_for_reward = "Yes" if average >= 90 and attendance >= 90 else "No"

# 3. Displaying output using different string formatting methods
print("\n" + "="*30)
print("       STUDENT REPORT")
print("="*30)

# Method 1: f-strings (Modern & Recommended)
print(f"Name: {name}")
print(f"Average Marks: {average:.2f}")

# Method 2: .format() method
print("Attendance: {}%".format(attendance))
print("Final Status: {}".format(status))

# Method 3: % operator (Old Style)
print("Grade: %s" % grade)
print("Eligible for Reward: %s" % eligible_for_reward)
print("="*30)