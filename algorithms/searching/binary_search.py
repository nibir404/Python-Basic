# Binary Search Algorithm implementation in Python
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Note: Requires a sorted input list

# 1. Provide a sorted list for binary search
numbers = [1, 4, 7, 10, 15, 18, 21]
target_number = int(input("Enter the number you want to find: "))

# 2. Define the left and right boundaries for the search
left = 0
right = len(numbers) - 1

# 3. Repeat while the search space is not empty
while left <= right:
    # 4. Calculate the middle index
    mid = (left + right) // 2
    
    # 5. Check if the element is at the middle.
    if numbers[mid] == target_number:
        print(f"Target number {target_number} was successfully found at index {mid}.")
        break
    
    # 6. If target is larger, search the right half
    elif numbers[mid] < target_number:
        left = mid + 1
    
    # 7. Otherwise, search the left half
    else:
        right = mid - 1
else:
    # 8. If search completes without break, record not found
    print(f"Target number {target_number} was not found in the list.")

