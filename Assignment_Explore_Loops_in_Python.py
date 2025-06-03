#Assignment: Explore Loops in Python
#Task 1: Counting Down With Loops
number = int(input("Please enter a number to count down from: "))
while number >= 0:
    if number == 0:
        print("Blast off!")
        break
    print(number, end=' ')
    number -= 1
print()
#Task 2: Multiplication Table with for Loops
number = int(input("Please enter a number to generate its multiplication table: "))
for i in range(1, 11):
    print(number, 'x', i, '=', number * i, end=' ')
print()
#Task 3: Find the Factorial
number = int(input("Please enter a number to find its factorial: "))
for i in range(1, number + 1):
    if i == 1:
        factorial = 1
    else:
        factorial *= i
print("The factorial of", number, "is", factorial)
print()