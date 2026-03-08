# Basic List Operations in Python
# Demonstrating indexing, appending, and removal

# 1. Initialize a list of items
cart = ['Laptop', 'Phone', 'Headphone', 'Keyboard', 'Mouse']

# 2. Accessing elements by index
print(cart[0]) # Output: Laptop
print(cart[4]) # Output: Mouse

# 3. Modify the list
cart.append('Cable')      # Adds 'Cable' to the end of the list
cart.remove('Headphone') # Removes the first occurrence of 'Headphone'

# 4. Display the modified list
print(cart)
