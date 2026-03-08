# Bubble Sort Algorithm implementation in Python
# Time Complexity: O(n^2) - Best case O(n) if optimized with a flag
# Space Complexity: O(1)

# 1. Bubble Sort: Ascending Order Example
numbers_asc = [9, 2, 7, 4, 1]
n = len(numbers_asc)

# Outer loop to traverse through all elements
for i in range(n):
    # Inner loop for comparisons and swaps
    for j in range(0, n - i - 1):
        # Swap if the element found is greater than the next element
        if numbers_asc[j] > numbers_asc[j + 1]:
            numbers_asc[j], numbers_asc[j + 1] = numbers_asc[j + 1], numbers_asc[j]

print('Ascending Order:', numbers_asc)


# 2. Bubble Sort: Descending Order Example
numbers_desc = [12, 7, 3, 15, 9]
m = len(numbers_desc)

# Outer loop to traverse through all elements
for i in range(m):
    # Inner loop for comparisons and swaps
    for j in range(0, m - i - 1):
        # Swap if the element found is LESS than the next element
        if numbers_desc[j] < numbers_desc[j + 1]:
            numbers_desc[j], numbers_desc[j + 1] = numbers_desc[j + 1], numbers_desc[j]

print('Descending Order:', numbers_desc)