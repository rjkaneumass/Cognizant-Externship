#Project: About Menu
import turtle
print("Welcome to my program! Please select an option:")
print("1. Calculate the factorial of a number")
print("2. Find the nth Fibonacci number")
print("3. Draw a recursive fractal pattern")
print("4. Exit")
user_choice = int(input("Enter your choice (1-4): "))
if user_choice not in [1, 2, 3, 4]:
    print("Invalid choice. Please run the program again and select a valid option.")
    exit()
#Step 2: Factorial Function: Used to calculate the factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
if user_choice == 1:
    num = int(input("Enter a number to find its factorial: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print("Factorial:", factorial(num))
    print("Thank you for using the program. Have a great day!")
#Step 3: Fibonacci Function: Used to find the nth Fibonacci number using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
if user_choice == 2:
    num = int(input("Enter the position of the Fibonacci number: "))
    if num < 0:
        print("Fibonacci number is not defined for negative positions.")
    else:
        print("Fibonacci number at position", num, ":", fibonacci(num))
    print("Thank you for using the program. Have a great day!")
#Step 4: Recursive Fractal Function: Used to draw a tree pattern using turtle graphics
def draw_tree():
    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(-100, 50)
    t.pendown()
    t.begin_fill()
    t.color("brown")
    t.pensize(2)
    t.forward(40)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(200)
    t.end_fill()
    t.penup()
    t.goto(-10, 50)
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.circle(70)
    t.end_fill()
if user_choice == 3:
    print("Drawing a recursive fractal pattern...")
    draw_tree()
    turtle.done()
    print("Fractal pattern drawn. Have a great day!")
if user_choice == 4:
    print("Thank you for using the program. Goodbye!")


