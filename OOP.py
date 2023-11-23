x = list()
type(x)
print(type(x))
print(dir(x))

class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    
    def party(self):
        self.x = self.x + 1
        print(self.name, "So far", self.x )

    #def __del__(self):
        #print('I am destructed', self.x)

s = PartyAnimal('Nicholas')
s.party()

j = PartyAnimal('James')
j.party()
#s =42
#print ('an contains', an) 

#print(type(an))
#print(dir(an))

class RugbyFan(PartyAnimal):
    points = 0
    def tryscored(self):
        self.points = self.points + 5
        self.party()
        print(self.name, 'points', self.points)

v = RugbyFan('Sam')
v.party()
print(v.tryscored())
