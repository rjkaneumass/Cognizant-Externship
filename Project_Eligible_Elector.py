#Project: Eligible Elector
#Step 1: Ask the User's Age
age = int(input("How old are you? "))
#Step 2: Decide the Eligibility
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    print("Oops! You're not eligible yet. But hey, you only have ", 18-age, " more years to go!")