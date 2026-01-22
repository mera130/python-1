class myClass:
    __privateVar = 27
    def __privmeth(self):
        print('i am inside my class')
    def hello(self):
        print('private variable value: ', myClass.__privateVar)
foo = myClass()
foo.hello()
foo.__privmeth