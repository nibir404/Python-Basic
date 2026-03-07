numbers = [1,4,7,10,15,18,21]
target_number = int(input("Enter any number: "))

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left+right) // 2
    if numbers[mid] == target_number:
        print("Number found at index", mid)
        break
    elif numbers[mid] < target_number:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Number not found")

