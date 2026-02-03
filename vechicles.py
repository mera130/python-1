class vechicle:
    def __init__(self, max_speed, milage):
        self.max = max_speed
        self.mil = milage
bmw = vechicle(240,18)
print('BMW max speed', bmw.max)
print('BMW milage', bmw.mil)
ferrari = vechicle(310,10)
print('ferarri max speed', ferrari.max)
print('ferrari milage', ferrari.mil)