def factorial(x):
    if x == 0 or x ==1:
        return 1 
    else:
        return x*factorial(x-1)

print(factorial.__doc__)
print("factorial of 0: ", factorial(0))
print("factorial of 1: ", factorial(1))
print("factorial of 4: ", factorial(4))
print("factorial of 5: ", factorial(5))
print("factorial of 10: ", factorial(10))