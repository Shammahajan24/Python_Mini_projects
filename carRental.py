class bikeShop:
    def __init__(self,stock):
        self.stock=stock
    def display(self):
        print("total Bikes",self.stock)
    def rentForBike(self,q):
        if q<=0:
            print("Enter the positive value or greater than zero")
        elif q>self.stock:
            print("Enter the value(less than stock)")
        else:
            print("Total Price",q*100)
            print("Total Bikes",self.stock)

while True:
    obj=bikeShop(200)
    uc=int(input('''
1.Display Stocks
2.Rent a Bike
3.Galti se aagaye Exit karo                                  
'''))
    if uc==1:
        obj.display()
    elif uc==2:
        n=int(input("Enter the Quantity"))
        obj.rentForBike(n)
    else:
        break    


