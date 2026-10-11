class rectangle:
    def __init__(self,length,berdth):
        self.length = length
        self.berdth = berdth
    def area(self):
        return self.length*self.berdth

class square:
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side*self.side


rec = rectangle(4,5)
sq = square(8)
print("area of rectangle is :",rec.area())
print("area of square is :",sq.area())
