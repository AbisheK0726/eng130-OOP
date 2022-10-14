from animal import Animal

class Reptile (Animal):
    
    def __init__(self, name):
        super().__init__(name)
        self.cold_blooded = True
        self.tetrapod = None
        
    def seek_heat(self):
        print("I seek heat")
    
    def hunt(self):
        print("I hunt for food")
        
    
