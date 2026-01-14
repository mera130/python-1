import random
import string

length = 10
password = ''

for i in range(length):
    choice = random.randint(1, 3)
    
    if choice == 1:
        password += random.choice(string.ascii_uppercase) 
    elif choice == 2:
        password += random.choice(string.ascii_lowercase)
    else:
        password += random.choice(string.digits) 

print(f"Your password: {password}")