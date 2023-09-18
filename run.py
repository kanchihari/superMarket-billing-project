from datetime import datetime

# Function to display the available items


def display_item_list():
    print("Available Items:")
    print(lists)

# Function to get the user's item choice


def get_user_item_choice():
    while True:
        item = input("Enter the item you want to buy: \n")
        if item in items:
            return item
        else:
            print("Invalid item! Please enter a valid item.")


# Main program 
print("--------------------- Welcome to SuperMarket ---------------------")

# Prompt the user for their name
name = input("Enter Your name: \n")

# List of items along with their prices in euros per unit or per kilogram/liter
lists = '''
1. Apples - 1.50 €/- per kg
2. Rice - 4.00 €/- per kg
3. Milk - 2.00 €/- per liter
4. Oil - 2.39 €/- per liter
5. Meat - 14.00 €/- per kg
6. Cola - 1.90 €/- per liter
7. Wine - 2.50 €/- 500ml
8. Curd - 1.40 €/- 500ml
9. Atta - 5.00 €/- per kg
10. Bread - 3.00 €/- per loaf
'''

# Dictionary to store item names and their respective prices in euros
items = {
    'Apple': 1.50,
    'Rice': 4.00,
    'Milk': 2.00,
    'Oil': 2.39,
    'Meat': 14.00,
    'Cola': 1.90,
    'Wine': 2.50,
    'Curd': 1.40,
    'Atta': 5.00,
    'Bread': 3.00
}

total_price = 0
pricelist = []
itemList = []
quanList = []
priceList = []

while True:
    option = input("To view the list of items, press 1: \n")

    # Check if the option is valid
    if option.isdigit() and int(option) in [1]:
        option = int(option)
        break
    else:
        print("Invalid option! Please enter a valid option .")

# Check if the user selected option 1 to view the list of items
if option == 1:
    display_item_list()  # Call the function to display the item list        