class AP():
    
    first= "Navi"
    last="Bar"
    def Age(self):
        print("Age is 19")
    def Games(self):
        print("Outdoor Games")
class SL(AP):
    first="Raitot"
    last="Tento"
    def Games(self,x=None):
        if(x==None):
            print("Online games")
        else:
            print("Name is",x)

B1= SL()
B="Genshin Impact"
print(B1.first)
print(B1.last)
B1.Age()
B1.Games(B)


"""class Primaryz():
    def barren(self):
        print("Barren land With nothing on it")
    def first(self):
        print("First Species to migrate to barren land")
class Secondary(Primaryz):
    def second(self):
        print("Second Species replaceing the first")
    
class Autotropic(Secondary):
    def Auto(self):
        print("Plants/vegetation takeing over after the secondary Species")
Species=Autotropic()
Species.barren()
Species.first()
Species.second()
"""



#class Intro():
#    def Attributes(self,x,y):

#        print("My Name is ",x)
#        print("I am ",y)

#    def selfInterest(self):
 #       print("My hobbies are Xyz")

#Name=input("")
#Age=int(input(""))
#PersonA= Intro()
#PersonA.Attributes(Name,Age)
#PersonA.selfInterest()