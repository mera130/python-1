class bird:
    def __init__(self):
        print('bird is ready')
    def whoIsThis(self):
        print('penguine is ready')
    def swim(self):
        print('swims faster')
class peguine(bird):
    def __init__(self):
        super().__init__()
        print(' peguinr is ready')
    def whoIsThis(self):
        print('penguine')
    def run(self):
        print('runs faster')
paggy = peguine()
paggy.whoIsThis()
paggy.swim()
paggy.run()
