num = [1,2,3,4,5,6]
even_squares = [x*x for x in num if x%2==0]
print(even_squares)

num2 = [-3,4,-1,6,0]
positives = [x for x in num2 if x >0]
print(positives)

names = ['cat', 'dog', 'tiger']
upper_names = [name.upper() for name in names]
print(upper_names)
