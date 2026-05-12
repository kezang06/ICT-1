detail = open("student.txt", "w")
detail.write("Kezang:1234\n")
detail.write("Dechen:5678\n")
detail.write("Jigme:9101\n")
detail.write("Yoezer:1121\n")
detail.write("Choden:3115\n")
detail.close()

print("Dummy file 'student.txt' created successfully!")


with open("student.txt", "r") as f:
    students = f.readlines()
search_name = input("Enter student name to search: ")

found = False
for line in students:
    if search_name.lower() in line.lower():  
        print("Student found")
        found = True
        break

if not found:
    print("Student not found in the file.")