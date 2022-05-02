class Primaryz():
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