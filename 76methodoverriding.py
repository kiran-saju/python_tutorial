#eg1
class Human:
    def use(self): #method
        print("Human can walk")
class Male(Human):
    def use(self): #method
        print("Man Can walk")
    
m1=Male()
m1.use() #overrided method
