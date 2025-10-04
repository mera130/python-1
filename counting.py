amount = int(input("enter the amount of money: "))
note1 = amount//100
note2 = (amount %100) // 50
note3 =  (amount %100) % 50 // 10

print("notes of 100 tk", note1)
print("notes of 50 tk", note2)
print("notes of 10 tk", note3)