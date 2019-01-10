# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.achoos.com"  # Give your site a name
picked_store=""

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)
    pick_store()
def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for n in range(len(stores)):
        print (stores[n])

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    #st=store_name
    print ("-------------------------------")
    print (store_name.upper() + ":")
    

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
    picked_store=input("Pick a store by typing its name. Or type \'checkout\' to pay your bills and say your goodbyes.")
    get_store(picked_store)

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    cart.add_to_cart(picked_store)

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    pick_products(cart,picked_store)
    cart.get_total_price()

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
