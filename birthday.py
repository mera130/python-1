birthdays = {}

birthdays["merhisa"] = (1990, 5, 15)  
birthdays["nuhi"] = (1920, 12, 3)
birthdays["alvena"] = (2002, 5, 8)

name = input("Enter name: ").lower()
if name in birthdays:
    y, m, d = birthdays[name]
    print(f"{name} is born on: {d}/{m}/{y}")
else:
    print("Not found")