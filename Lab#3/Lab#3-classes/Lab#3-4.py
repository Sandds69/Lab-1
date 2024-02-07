class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return (self.x, self.y)

    def move(self, x2, y2):
        self.x = x2
        self.y = y2
    
    def dist(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    
    #Тоже самое но матем задача про поиск длины между точками