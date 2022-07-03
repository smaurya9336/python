class Mobile:
    def __init__(self,m):
        self.model=m
    
    def show_model(self,p):
        self.price=p
        print("Model:",self.model,"Price:",self.price)

realme=Mobile('ReadMe X')
realme.show_model(1000)
print(id(realme))
print()
redmi=Mobile('Readmi 7s')
redmi.show_model(2000)
print(id(redmi))
print()

geek=Mobile('Python')
geek.show_model(49)
print(id(geek))


