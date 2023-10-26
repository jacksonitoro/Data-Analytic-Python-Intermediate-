class Water_Bottle:
    def __init__(self,capacity):
        self.capacity = capacity

    def fill_up(self, other_bottle):
        #self.other_bottle = other_bottle
        self.capacity=other_bottle.capacity + self.capacity

bottle1 = Water_Bottle(500)
bottle2 = Water_Bottle(250)
print(bottle1.capacity)
bottle1.fill_up(other_bottle=bottle2)

print(bottle1.capacity)


     
        


