try:
    age = int(input('enter your age:'))
    if age %2==0:
        print("your age number is even")
    else:
        print('your age number is odd')
except ValueError:
    print('your age input is not valid')
    