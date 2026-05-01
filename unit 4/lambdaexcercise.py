check_no = lambda x: "positive" if x > 0 else("negative" if x < 0 else"zero")
user_input = int(input("Enter your number: "))
print(check_no(user_input))
