import pandas as pn
data = {
    'names': ['fatema', 'karim' ,'rahim', 'rodia', 'hasan'] ,
    'age': [21, 20, 22, 20, 20],
    'department': ['cse', 'bba', 'eee', 'eee', 'bba'],
    'math' : [90, 70, 80, 82, 68],
    'science' : [81, 76, 95, 89, 45]
}

df = pn.DataFrame(data)

print('original data: ')
print(df)

print('\n data set: ')
print(df.info())

print('\n statistic data: ')
print(df.describe())

print('\n names and age:')
print(df[['names', 'age']])

print('\n students older than 20')
print(df[df['age'] > 20])

df['total'] = df['math'] + df['science']
print('\n total marks : ')
print(df)

