#import pprint
class Table:
    def __init__(self, header, *data): #constructor with any number of 'data' values
        self.header = header
        self.data = data
        # max_header = max(self.header, key = len)
        # print("max header item length: ", max_header)

    def __str__(self):
        for n in self.header:
            print("{0:^11}".format(n), end='  ')
        print()
        for n in self.header:
            print("="*11, end='  ')
        print()
        for m in zip(*self.data):
            for x in range(len(m)):
                print("{0:^11}".format(m[x]), end='  ')
            print()            
t1 = Table(['first name', 'second name'], ['sandeep', 'kalyani', 'sahil'], ['gupta', 'kansal', 'singla'])  
t2 = Table(['vegetables', 'fruits', 'grains'],['potato', 'carrot', 'radish', 'eggplant'], ['fig', 'mango', 'plum', 'cherry'], ['rice', 'wheat', 'quinoa', 'oat'])

t1.__str__()
print()
t2.__str__()
