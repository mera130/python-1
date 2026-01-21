class vechicle:
    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage
class bus(vechicle):
    pass
school_bus = bus('school volvo', 188, 12)
print('vechicle name: ', school_bus.name, 'max speed: ', school_bus.max_speed, 'milage: ', school_bus.milage)
        