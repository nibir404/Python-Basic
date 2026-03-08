# List Iteration and Manipulation in Python
# Demonstrating basic operations like length check, iteration, and modifications

# 1. Initialize a list of tasks
tasks =['Study Python', 'Go to gym', 'Read Book', 'Practice DSA']

# 2. Iterate through the tasks list
for task in tasks:
    print(task)

# 3. Check the number of items in the list
print("Number of tasks:", len(tasks))

# 4. Access individual items by index
print("Second task:", tasks[1])

# 5. Add and remove items from the list
tasks.append('Build a project') # Append adds to the end
tasks.remove('Go to gym')      # Remove by value

# 6. Final display of the modified list
print("Final tasks:", tasks)