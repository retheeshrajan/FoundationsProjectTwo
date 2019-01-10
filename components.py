# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name=name

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        self.product=product
        #print_products()
    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        return "Name:" + self.product.name + " - " + self.product.description + " - " + str(self.product.price) 

    def __str__(self):
        return "- " + self.name

class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        self.name=name
        self.description=description
        self.price=price

    def __str__(self):
        # your code goes here!
        return "Name:" + self.name + " - " + self.description + " - " + str(self.price) 

class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.product=product

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total=0
        for p in self.product:
            total=total+self.product.price

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!

    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!
