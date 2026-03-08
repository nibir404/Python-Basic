# Linear Search Algorithm implementation in Python
# Time Complexity: O(n)
# Space Complexity: O(1)

# 1. Define the collection to search
numbers_list = [3, 7, 12, 25, 30]

# 2. Get the target number from the user
target_number = int(input("Enter the number you want to find: "))

# 3. Initialize a flag to track if the number is found
is_found = False

# 4. Iterate through the entire list to find the match
for item in numbers_list:
    if item == target_number:
        is_found = True
        break

# 5. Output the search result
if is_found:
    print(f"Target number {target_number} was successfully found in the list.")
else:
    print(f"Target number {target_number} was not found.")