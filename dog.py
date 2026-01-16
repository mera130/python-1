class dog:
    species = 'dog'
    def __init__(self,breed ,age):
        self.breed = breed
        self.age = age
dog1 = dog('german shephard', 3)
dog2 = dog('golden retriever', 5)
dog3 = dog('french pitbull', 2)
# dog 1
print('about dog 1')
print('species:', dog1.species)
print('breed:', dog1.breed)
print('age:', dog1.age, 'years')

# dog 2
print('about dog 2')
print('species:', dog2.species)
print('breed:', dog2.breed)
print('age:', dog2.age, 'years')

# dog 1
print('about dog 3')
print('species:', dog3.species)
print('breed:', dog3.breed)
print('age:', dog3.age, 'years')


