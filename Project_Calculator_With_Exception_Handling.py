#Project: Calculator With Exception Handling
#Step 1: Menu of Operations
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='error_log.txt', filemode='w')
logging.info("Calculator started")
print("Welcome to the Calculator!")
print("Please select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
#Step 2: Input Validation
def calculator():
    user_operation = input("Enter the number corresponding to your operation: ")
    try:
        user_operation = int(user_operation)
        if user_operation < 1 or user_operation > 5:
            raise ValueError()
    except ValueError:
        logging.error("Invalid input: %s", user_operation)
        print("Invalid input. Please enter a number between 1 and 5.")
        return calculator()
    if user_operation == 1:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 + num2
        except ValueError:
            logging.error("Invalid input for numbers.")
            print("Invalid input. Please enter valid numbers.")
            return calculator()
        else:
            print("The result of addition is: ", result)
        finally:
            print("Thank you for using the calculator!")
            return calculator()
    elif user_operation == 2:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 - num2
        except ValueError:
            logging.error("Invalid input for numbers.")
            print("Invalid input. Please enter valid numbers.")
            return calculator()
        else:
            print("The result of subtraction is: ", result)
        finally:
            print("Thank you for using the calculator!")
            return calculator()
    elif user_operation == 3:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 * num2
        except ValueError:
            logging.error("Invalid input for numbers.")
            print("Invalid input. Please enter valid numbers.")
            return calculator()
        else:
            print("The result of multiplication is: ", result)
        finally:
            print("Thank you for using the calculator!")
            return calculator()
    elif user_operation == 4:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 / num2
        except ValueError:
            logging.error("Invalid input for numbers.")
            print("Invalid input. Please enter valid numbers.")
            return calculator()
        except ZeroDivisionError:
            logging.error("Division by zero error")
            print("Oops! Division by zero is not allowed.")
            return calculator()
        else:
            print("The result of division is: ", result)
        finally:
            print("Thank you for using the calculator!")
            return calculator()
    elif user_operation == 5:
        print("Thank you for using the calculator! Hope to see you again!")
        return
calculator()

    

