while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choice = input("Choose an operation (1-5): ")

    if choice == '5':
        print("exit")
        break

    N1 = float(input("Enter number: "))
    N2 = float(input("Enter number: "))

    def add():
        return N1 + N2

    def subtract():
        return N1 - N2

    def multiply():
        return N1 * N2

    def divide():
        if N2 == 0:
            return "Error! Cannot divide by zero"
        return N1 / N2

    if choice == '1':
        print("Total added number:", add())

    elif choice == '2':
        print("Total Subtracted number:", subtract())

    elif choice == '3':
        print("Total multiplied number:", multiply())

    elif choice == '4':
        print("Total divided number:", divide())