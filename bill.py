unit = int(input("enter the unit: "))

if unit <= 50:
    amount  = 50*2.60
    surcharge = 25
elif unit <= 100:
    amount = 130+((unit - 50)* 3.25)
    surcharge = 35
elif unit <= 200:
    amount = 130+162.5+((unit - 100)* 5.26)
    surcharge = 45
else:
    amount =130 + 162.5 + 526+((unit - 200)* 8.45)
    surcharge = 75
    
total_bill = surcharge + amount
print("\n electricity bill = %.2f"% total_bill)
    