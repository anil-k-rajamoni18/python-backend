class Person1():
   
    def __init__(self,surname,age): # param
        self.c=surname
        self.d=age
        
    def __init__(self): # non-param
        print("Hey HI!!")
             
    def __init__(self,name): # param
        self.a=name      
        
    def __init__(self,fullname,year,place): # param
        """
        constructor
        """
        self.x=fullname
        self.y=year
        self.z=place


p = Person1('Alice', 45)
print(p)