from reptaile import Reptile

class sk(Reptile):
    
    def __init__(self, name):
        super().__init__(name)
        self.forked_tongue = True
        
    def use_tongue_to_smell(self):
        print ("I use my tongue to smell")

smart_reptile = sk("Smart Reptile")
print(smart_reptile.move())
print(smart_reptile.seek_heat())