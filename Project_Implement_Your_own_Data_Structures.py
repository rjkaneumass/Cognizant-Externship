#Project: Implement Your own Data Structures
#Step 1: Create the Inventory
inventory = {}
#Step 2: Add, Remove, and Update Items
inventory['AT-AT'] = (2, 500)
inventory['Venator'] = (3, 650)
print("Welcome to the Inventory Manager!")
print("Current Inventory:")
total_value = 0
#Step 3: Display the Inventory
for item, (quantity, price) in inventory.items():
    print("Item:", item, "Quantity:", quantity, "Price: $", price)
    total_value += quantity * price
print("Total Value of Inventory: $", total_value)
inventory['Jango-Fett Starship'] = (5, 300)
inventory.pop('AT-AT')
inventory.update({'Venator': (4, 650)})
total_value = 0
print("Updated Inventory:")
for item, (quantity, price) in inventory.items():
    print("Item:", item, "Quantity:", quantity, "Price: $", price)
    total_value += quantity * price
print("Total Value of Inventory: $", total_value)