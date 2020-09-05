class Table:
    def __init__(self, header, *data): #constructor with any number of 'data' values
        self.header = header
        self.data = data


    def __str__(self):
        
        for n in self.header:
            print(n, end='      ')
        print()
        for n in self.header:
            print("=========", end='      ') #Doesn't take the size of the headers so not pretty enough
        print()
        for m in self.data:
            for x in m:
                print(x, end='      ')
            print()
            


t1 = Table(['first name', 'second name'], ['sandeep', 'kalyani', 'sahil'], ['gupta', 'kansal', 'singla'])  
t2 = Table(['vegetables', 'fruits', 'grains'],['potato', 'carrot', 'radish', 'eggplant'], ['fig', 'mango', 'plum', 'cherry'], ['rice', 'wheat', 'quinoa', 'oat'])

t1.__str__()