number = input("Enter any number: ")
count = 0
i = 0

while i < len(number):
    if number[i] in "0123456789":
        count += 1
    i += 1

print("number of dgits:", count)