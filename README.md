# SuperMarket Billing System

This Python script implements a simple SuperMarket Billing System. It allows users to view a list of available items with their prices and make purchases by selecting items and quantities.

## Table of Contents
- [Code Structure](#code-structure)
- [Functionality](#functionality)
- [Flowchart](#flowchart)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Code Structure

The code is organized into several functions and a main program:

1. **`display_item_list()`**: Displays the available items and their prices.
   
2. **`get_user_item_choice()`**: Prompts the user to enter the item they want to buy and validates the input.

3. **`get_user_item_quantity()`**: Prompts the user to enter the quantity of the item they want to buy and validates the input.

4. **Main Program**:
   - Prompts the user for their name and displays a welcome message.
   - Displays the list of available items.
   - Allows the user to either view the list of items or exit the program.
   - Handles the user's choice to buy items or exit.
   - Calculates the total price and generates a bill if the user chooses to buy.

## Functionality

1. The program begins by prompting the user for their name and displaying a welcome message.

2. It then displays the available items and their prices.

3. The user can choose to view the list of items or exit the program. If they choose to view the list, the program displays the available items.

4. If the user chooses to buy items, they can select items and quantities. The program calculates the total price and generates a bill.

5. The bill includes item-wise details, the total price, GST (5%), and the final price.

6. The program ends by thanking the user for visiting the supermarket.

## Flowchart

A flowchart visually represents the flow of the program. Since creating a flowchart in this text format is limited, it's recommended to use a diagramming tool to create an accurate and detailed flowchart.

For creating a flowchart, you can use various tools like draw.io, Lucidchart, or any flowchart tool of your choice. Here's a textual representation to give you an idea:

1. **Start**:
   - Get user's name.

2. Display welcome message and available items.

3. Prompt user for option:
   - If option is 1, display item list.
   - If option is 2, exit and display exit message.

4. If option is 1:
   - Get user's item choice and quantity.
   - Calculate price for each item.
   - Calculate total price.

5. Prompt user to generate bill:
   - If yes, calculate GST and final price.
   - Print bill details.

6. Thank the user for visiting the supermarket.

7. **End**.

## Usage

To run the SuperMarket Billing System, execute the Python script. Follow the prompts to interact with the system and make purchases.

## Contributing

Contributions are welcome! Feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
