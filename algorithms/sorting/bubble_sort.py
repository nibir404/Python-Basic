list = [9,2,7,4,1]
n = len(list)
for i in range(n):
    for j in range(0, n-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(list)

numbers = [5,1,8,3]
m= len(numbers)
for i in range(m):
    for j in range (0, m-i-1):
        if numbers[j] < numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
print('Ascending order:', numbers)

numbers = [12,7,3,15,9]
m= len(numbers)
for i in range(m):
    for j in range (0, m-i-1):
        if numbers[j] < numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
print('Descending:', numbers)