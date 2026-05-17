age = int(input("Enter your age: "))
if age >=18:
    registered_voter = input("Are you a registered voter? (True/False): ")
    registered_voter = registered_voter.lower() 
    if registered_voter == "true":
        print("You are eligible to vote.")
    elif registered_voter == "false":
        print("you need to register to vote.")

else:
    print("You are not eligible to vote yet.")