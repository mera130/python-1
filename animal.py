from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print('i can walk and move ')
class snake(animal):
    def move(self):
        print('i can crawl ')
class dog(animal):
    def move(self):
        print('i bark ')
class lion(animal):
    def move(self):
        print('i can roar ')
r = human()
r.move()
k = snake()
k.move()
r = dog()
r.move()
k = lion()
k.move()