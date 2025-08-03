# online-shopping-cart-final
Final portfolio project for CSC500: Principles of Programming. Implements an online shopping cart in Python using object-oriented programming with classes, methods, and a menu-driven interface. Features dynamic date handling and a predefined product database using product IDs.
# Online Shopping Cart - Final Project (CSC500)

This project is the final portfolio milestone for CSC500: Principles of Programming at CSU Global. It demonstrates object-oriented programming in Python by simulating a simple online shopping cart system.

## Features

- **Classes**:
  - `ItemToPurchase`: Represents individual products with name, price, quantity, and description.
  - `ShoppingCart`: Manages the customer’s cart, including adding, removing, modifying items, and calculating totals.
  
- **Menu-Driven Interface**:
  - Add items using **product IDs** from a predefined mini database.
  - Remove or modify items in the cart by selecting their cart index.
  - Output the cart’s total cost or item descriptions.
  - Looping menu until the user chooses to quit.

- **Dynamic Date**:
  - Automatically fetches today’s date (similar to Excel’s `=TODAY()`).

- **Predefined Product Database**:
  - Three sample products preloaded with IDs, names, descriptions, and prices.

## How to Run

1. Clone this repository or download the ZIP file.
2. Open the project in Visual Studio Code or your preferred Python IDE.
3. Run the Python script:

```bash
python shopping_cart.py
