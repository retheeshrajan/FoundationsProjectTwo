from data import stores
site_name = "www.achoos.com"
print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)
for n in range(len(stores)):
    print (stores[n])
picked_store=input("Pick a store by typing its name. Or type \'checkout\' to pay your bills and say your goodbyes.")
    