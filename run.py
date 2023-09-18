from datetime import datetime

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