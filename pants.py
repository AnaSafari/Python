class Pants:
    def __init__(self,color, waistSize, length, price):
        self.color = color
        self.waist_size = waistSize
        self.length = length
        self.price = price
        
    def change_price (self, newPrice):
        self.price = newPrice
        
    def discount(self, discountPercent):
        discountedPrice = (1-discountPercent)*self.price
        return discountedPrice

def main():
    pass

if __name__ = "__main__":
    print("Running Pant Class Main File")