class Point:
    def __init__(self, position, move):
        self.position = position
        self.move = move
        
        
    
    def Show(self):
        return self.position
        
    def Move(self):
        return self.move
        
    def Dist(self):
        return self.move - self.position
        
        




point = Point(52, 66)

print("position and distance:", point.Show(), point.Dist())  


