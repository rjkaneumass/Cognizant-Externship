#Assignment: Check Your Knowledge on Errors
#Task 1: Understanding Python Exceptions
user_input = input("Enter a number: ")
try:
    final_number = 100 / int(user_input)
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
else:
    print("100 divided by ", user_input, " is ", final_number)
#Task 2: Types of Exceptions
cool_characters = ['Anakin', 'Obi-Wan', 'Yoda', 'Darth Vader', 'Luke']
print("Cool characters in the list:")
for character in cool_characters:
    print(character)
print("Please enter an index to print a character just for you: ")
user_input = int(input())
try:
    print("You entered: ", cool_characters[user_input])
except IndexError:
    print("IndexError Occured! The list index is out of range.")
    #Occurs when the user inputs an index that is not in the list.
x = 25
print("Enter a number to add to 25: ")
user_input = input()
try:
    x += user_input
except TypeError:
    print("TypeError Occured! Unsupported operant types.")
    #Occurs when the user inputs a string instead of a number.
dictionary = {'name': 'Rob', 'age': 21, 'height': 5.10}
print(dictionary)
print("Enter a key to access its value: ")
user_input = input()
try:
    print("The value for the key '", user_input, "' is: ", dictionary[user_input])
except KeyError:
    print("KeyError Occured! Key not found in the dictionary.")
    #Occurs when the user inputs a key that is not in the dictionary.
#Task 3: Using try, except, else, and finally
user_input_1 = input("Please enter a number: ")
user_input_2 = input("Please enter another number: ")
try:
    result = int(user_input_1) / int(user_input_2)
except ValueError:
    print("ValueError Occured! Please enter valid numbers.")
except ZeroDivisionError:
    print("ZeroDivisionError Occured! You cannot divide by zero.")
else:
    print("The result is: ", result)
finally:
    print("Thank you for using this program! Hope you have a great day!")
