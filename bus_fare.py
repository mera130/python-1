class BusFare:
    def __init__(self, fare):
        self.fare = fare
    
    def total(self):
        return self.fare * 1.10 

class ChildBusFare(BusFare):
    def total(self):
        return (self.fare * 0.5) * 1.10 
adult = BusFare(100)
print(f"Adult: ${adult.total():.2f}")

child = ChildBusFare(100)
print(f"Child: ${child.total():.2f}")