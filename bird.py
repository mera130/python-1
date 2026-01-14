class parrot:
    species = 'parrot'
    def __init__(self, name,age):
        self.age = age
        self.name = name 
jin = parrot('jin', 10)
woo = parrot('woo', 15)
print('jin is a ', jin.species)
print('woo is also a ', woo.species)
print(jin.name ,"is", jin.age )
print(woo.name, 'is', woo.age)
        
    