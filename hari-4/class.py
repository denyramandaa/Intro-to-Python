class car:
    def __init__(self, color, x, y, isOn):
        self.color = color
        self.x = x
        self.y = y
        self.isOn = isOn
        
    def turn_on(self):
        self.isOn = True
        return self
        
    def turn_of(self):
        self.isOn = False
        return self
        
    def move(self,x,y):
        self.x = self.x + x
        self.y = self.y + y
        return self
        
my_car = car('red', 0, 0, False)


print(my_car.isOn)

my_car.turn_on()
print(my_car.isOn)