class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price
    
    def change_price(self, new_price):
    
        self.price = new_price
        
    def discount(self, discount):

        return self.price * (1 - discount)


##instanciate two objects 
shirt_one = Shirt('red', 'S', 'long-sleeve', 25)
shirt_two = Shirt('orange', 'L', 'short-sleeve', 10)

## Printing price and then changing it to 10 
print("price of the shirt is {}".format(shirt_one.price))
shirt_one.change_price(10)
print("Updated price is {}".format(shirt_one.price))


### finding the total price and total discount
### use the shirt discount method to calculate the total cost if
### shirt_one has a discount of 14% and shirt_two has a discount of 6%
total = shirt_one.price + shirt_two.price
total_discount = shirt_one.discount(0.14) + shirt_two.discount(0.06)


def main():
	pass

if __name__ == '__main__':
	print("total_price is {}".format(total))
	print("totla_price_after_discount is {}".format(total_discount))
