# Menu defining items sold in a cafe.
menu = {"Tea", "Coffee", "Sandwich", "Muffin"}

# Below is the dictionary listing stock values.
stock = {
    "Coffee": 150,
    "Tea": 160,
    "Sandwich": 55,
    "Muffin": 75
}

# Defining the price of each menu item.
price = {
    "Coffee": 2.20,
    "Tea": 2.00,
    "Sandwich": 3.90,
    "Muffin": 2.50
}

# Initialising stock count using a variable.
total_stock = 0

# For loop used to calculate the net value of stock.
for item in menu:
    item_value = (stock[item] * price[item])
    total_stock += item_value


print("The net value of stock in the cafe: £{:.2f}".format(total_stock))
