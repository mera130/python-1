class computer:
    def __init__(self):
        self._maxprice = 900
    def sell(self):
        print('selling price: '.format(self._maxprice))
    def setmaxprice(self,price):
        self._maxprice = price
c = computer()
c.sell()
c._maxprice = 1000
c.sell()
c.setmaxprice(1000)
c.sell()