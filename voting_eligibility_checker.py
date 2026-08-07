# Python Voting Eligibility Checker

age = int(input("Enter your age: "))

if age >= 18:
    voter_id = input("Do you have a Voter ID? (Y/N): ").lower()

    if voter_id == "y":
        print("You are eligible to vote.")
    else:
        print("Please apply for a Voter ID.")
else:
    print("You are not eligible to vote.")
