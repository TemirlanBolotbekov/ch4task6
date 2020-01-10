class House():
    def __init__(self, typehouse, areahouse):
        self.typehouse = typehouse
        self.areahouse = areahouse

    def get_house(self):

        self.totalarea = 0
        self.furnitures = {
            'bed' : 4,
            'wardrobe' : 2,
            'table' : 1.5
        }
        for value in self.furnitures.values():
            self.totalarea += value
        

        print(f'Type: {self.typehouse} -- Total Area: {self.areahouse}\n{list(self.furnitures.keys())}\nArea: {self.areahouse - self.totalarea}')

        




var1 = House('Kvartira', 80)
var1.get_house()
