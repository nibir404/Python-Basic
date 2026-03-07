list = [3,7,12,25,30]
number = int(input("Enter any number: "))

found = False
for i in list:
    if i == number:
        found = True
        break
if found:
    print("Number found")
else:
    print("Number not found")