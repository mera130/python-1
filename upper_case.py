class IOstring():
    def __init__(self):
        self.st1 = ""
    def get_stringe(self):
        self.st1 = input('enter any string:')
    def print_string(self):
        print('result is : ', self.st1.upper())
st1  = IOstring()
st1.get_stringe()
st1.print_string()
    