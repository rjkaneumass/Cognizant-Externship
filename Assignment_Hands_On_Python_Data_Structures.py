#Assignment: Hands On Python Data Structures
#Task 1: Working with Lists
fruit_list = ['apple', 'strawberry', 'grape', 'cherry', 'watermelon'] #ABSOLUTELY THE BEST FRUIT LIST NO QUESTION
print("Original fruit list:", fruit_list)
fruit_list.append('raspberry') #This one is pretty good too
print("After appending raspberry:", fruit_list)
fruit_list.remove("apple")
print("After removing apple:", fruit_list)
reversed_fruit_list = fruit_list[::-1]
print("Reversed fruit list:", reversed_fruit_list)
print()
#Task 2: Exploring Dictionaries
myself_dict = {
    'name': 'Robert Kane',
    'age': 21,
    'city': 'East Longmeadow'
}
print("Myself dictionary:", myself_dict)
myself_dict['favorite color'] = 'blue'
print("After adding favorite color:", myself_dict)
myself_dict.update({'city': 'Amherst'})
print("After updating city to Amherst:", myself_dict)
key_list = []
value_list = []
for key, value in myself_dict.items():
    key_list.append(key)
    value_list.append(value)
print("Keys:", key_list)
print("Values:", value_list)
print()
#Task 3: Using Tuples
tuple_for_me = ('Return of the King', 'Bad Decisions', 'Dune')
print("Favorite things tuple:", tuple_for_me)
#tuple_for_me[0] = 'Revenge of the Sith'
print("Oops! Tuples cannot be changed.")
print("Length of the tuple:", len(tuple_for_me))