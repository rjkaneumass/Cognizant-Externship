#Assignment: Exploring String Methods
#Task 1: String Slicing and Indexing
string_1 = "Python is amazing!"
first_extraction = string_1[0:6]
second_extraction = string_1[10:17]
reverse = string_1[::-1]
print("First word:", first_extraction)
print("Amazing part:", second_extraction)
print("Reversed string:", reverse)
print()
#Task 2: String Methods
string_2 = " hello, python world! "
print("Original string:", string_2)
strip_string = string_2.strip()
print("Stripped string:", strip_string)
capitalized_string = strip_string.capitalize()
print("Capitalized string:", capitalized_string)
universe_string = capitalized_string.replace("world", "universe")
print("Replaced 'world' with 'universe':", universe_string)
uppercase_string = universe_string.upper()
print("Uppercase string:", uppercase_string)
print()
#Task 3: Check for Palindromes
user_word = input("Enter a word to check if it's a palindrome: ")
reversed_word = user_word[::-1]
if user_word == reversed_word:
    print("Yes,", user_word, "is a palindrome!")
else:
    print("Sorry no,", user_word, "is not a palindrome.")