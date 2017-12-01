# Assignment: Product
# The owner of a store wants a program to track products. Create a product class to fill the following requirements.

# Product Class:
# Attributes:

#  Price

#  Item Name

#  Weight

#  Brand

#  Status: default "for sale"
# Methods:

#  Sell: changes status to "sold"

#  Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax

#  Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been, opened, set the status to "used" and apply a 20% discount.

#  Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.

class Product(object):


    def __init__(self, price, item_name, weight, Brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = Brand
        self.status = "for sale"
#methods   
    def change_status(self):  
        self.status = "sold" 
    def tax(self,tax):
        print "adding tax here"   
        self.price= self.price * tax + self.price 
        
        print self.price


milk = Product(3,"milk", 7, "Gallagher's")
print milk.tax(.06)
     
    







