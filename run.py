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
# Function to get the user's desired quantity for the item


def get_user_item_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity you want to buy: \n"))
            if quantity > 0:
                return quantity
            else:
                print("Invalid quantity! Please enter a valid quantity.")
        except ValueError:
            print("Invalid input! Please enter a valid numeric quantity.")


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
    'Oil': 2.50,
    'Meat': 14.00,
    'Cola': 1.50,
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

# Initialize 'buying' to False
buying = False

while True:
    print("Select an option:")
    print("1. Buy items")
    print("2. Exit")

    # Prompt the user for input
    input_str = input("Enter your choice (1 or 2): \n")

    # Check if the input is an integer
    if input_str.isdigit():
        input1 = int(input_str)
        # Check if the input is either 1 or 2
        if input1 in [1, 2]:
            if input1 == 2:
                print("Thank you for visiting our SuperMarket.Visiti Again.")
                break
            else:
                buying = True
                while buying:
                    item = get_user_item_choice()
                    quantity = get_user_item_quantity()
                    price = quantity * items[item]
                    pricelist.append((item, quantity, items[item], price))
                    total_price += price
                    itemList.append(item)
                    quanList.append(quantity)
                    priceList.append(price)

                    input2 = input("Want to buy more items(yes or no): \n")
                    if input2.lower() == 'no':
                        buying = False

                input3 = input("Do you want to bill the items (yes or no): \n")

                if input3.lower() == 'yes':

                    # Calculate GST (5%) and the final price

                    Gst = (total_price * 5) / 100
                    final_price = round(Gst + total_price, 2)

                    # Print the bill details
                    print("=" * 75)
                    print(" " * 27, "My SuperMarket")
                    print(" " * 30, "Kanchi")
                    print("Name:", name, 30 * " ", "Date:", datetime.now())
                    print(75 * "-")
                    print("S.no:", 6 * " ", "Item", 14 *
                          " ", "Quantity", 14 * " ", "Price")
                    print(75 * "-")

                    # Print the bill details for each purchased item
                    for i in range(len(pricelist)):
                        print("{:<12} {:<22} {:<20} {} €/-".format
                              (i + 1, itemList[i], quanList[i], priceList[i]))

                    # Print separators and the total price, GST & final price
                    print(75 * "-")
                    print("Total Price: {:<53}{} €/-".format(' ', total_price))
                    print("GST Tax (5%):{:<52} {} €/-".format(' ', Gst))
                    print(75 * "-")
                    print("Final Price: {:<52}{} €/-".format(' ', final_price))
                    print(75 * "=")

                    # Thank the user for visiting the supermarket
                    print("{}Thanks for visiting Our Store".format(' ' * 25))
                    break
                else:
                    print("Thank you for visiting. Have a great day!")
                    break
        else:
            print("Invalid input! Please enter a valid option (1 or 2).")
    else:
        print("Invalid input! Please enter a valid option (1 or 2).")
