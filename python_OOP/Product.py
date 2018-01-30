#class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax_rate):
        if tax_rate >= 1:
            return self.price + self.price * (tax_rate / 100)
        if tax_rate < 1:
            return self.price + self.price * tax_rate

    def make_return(self, note):
        if note == "defective":
            self.status = "defective"
            self.price = 0
        elif note == "in box":
            self.status = "for sale"
        elif note == "open box":
            self.status = "used"
            self.price = self.price - (self.price * 0.2)
        return self

    def display_info(self):
        print "Product name: {}".format(self.name)
        print "Product brand:", self.brand
        print "Price: ${}".format(self.price)
        print "Item weight {}oz.".format(self.weight)
        print "Item status:", self.status


beverage = Product(4.50, "Orange drink", 28, "Tampico")
beverage.display_info()
beverage.sell().return("defective").display_info()



