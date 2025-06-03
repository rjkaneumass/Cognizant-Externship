#Assignment: About Parameters of Functions
#Task 1: Writing Functions
def greet_user(name):
    print("Hello, ", name, "! How you are having a great day!")
def add_numbers(num1, num2):
    print("The sum of", num1, "and", num2, "is", num1 + num2)
greet_user("Robert")
add_numbers(12, 25)
print()
#Task 2: Using Default Parameters
def describe_pet(pet_name, pet_type="dog"):
    print("I have a", pet_type, "named", pet_name)
describe_pet("Tanner")
describe_pet("Ziggy", "dog")
print()
#Task 3: Functions with Variable Arguments
def make_sandwich(*ingredients):
    sandwich_ingredients = []
    for ingredient in ingredients:
        sandwich_ingredients.append(ingredient)
    print("Making a sandwich with the following ingredients:")
    for ingredient in sandwich_ingredients:
        print("-", ingredient)
make_sandwich("tuna", "pickles", "bacon")
print()
#Task 4: Understanding Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("The factorial of 10 is", factorial(10))
print()
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("The 7th number in the Fibonacci sequence is", fibonacci(7))
