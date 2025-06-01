# Assignment: Exploring Python Concepts

#Task 1: Variables: Your First Python Intro
name = "Robert"
age = 21
height = 5.11
print("Hey there Cognizant Team!! Excited to be a part of this journey. My name is", name, "and I am", age, "years old. My height is ", height, "feet tall.")

#Task 2: Operators: Playing with Numbers
#Addition
num1 = 9
num2 = 10
print("Hey team, what's 9 + 10? ", num1 + num2,"! Wait it isn't 21??")
#Subtraction
print("If I have 9 apples and I ate 10, how many do I have left? ", num1 - num2, ". Wait how is that possible??")
#Multiplication
print("If I have 9 bananas and I have them 10 times a day, how many bananas did I eat?", num1 * num2, ". Wait maybe I shouldn't have eaten that many bananas!?")
#Division
print("If I have 9 pizza slices and I have 10 friends, how many slices does each friend get? ", num1/num2, ". Wait this isn't elementary school anymore, we can just get more pizza!!")

#Task 3: Conditional Statements: The Number Checker
print("Hey y'all, let's check whether a number is positive, negative, or zero.")
number_given = int(input())
if number_given > 0:
    print("This number is positive. Awesome!")
elif number_given < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero is is. A perfect balance!")