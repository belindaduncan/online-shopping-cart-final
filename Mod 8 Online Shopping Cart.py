# Online Shopping Cart:
# Belinda Duncan 
# ================================
# Program Classes
# ================================
from datetime import datetime
# -------- ItemToPurchase Class --------
class ItemToPurchase:  # this is like an object template for items in the cart
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(total)}")

    def get_total_cost(self):
        return self.item_price * self.item_quantity


# -------- ShoppingCart Class --------
# Step 4: Build the ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        self.cart_items = []

# Classes do not inherit from each other, but they are expected to interact. The parameter "item" works because it is an instance of the ItemToPurchase class.
    def add_item(self, item):   
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, modified_item):
        found = False
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                found = True
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0.0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.get_total_cost() for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

# ================================
# Product Mini Database
# ================================

products = {
    1: {
        "name": "Nike Romaleos",
        "description": "Volt color, Weightlifting shoes",
        "price": 189
    },
    2: {
        "name": "Chocolate Chips",
        "description": "Semi-sweet",
        "price": 3
    },
    3: {
        "name": "Powerbeats 2 Headphones",
        "description": "Bluetooth headphones",
        "price": 128
    }
}


# ================================
# function supporting the main program
# -------- Menu Function --------
def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )

    option = ""
    while option != "q":
        print(menu)
        option = input("Choose an option:\n").lower()

        # Add item option
        if option == "a":
            print("Available products:")
            for pid, details in products.items():
                print(f"{pid} - {details['name']}")

            try:
                choice = int(input("Enter the product ID you want to add:\n"))
                if choice in products:
                    item = ItemToPurchase()
                    item.item_name = products[choice]["name"]
                    item.item_description = products[choice]["description"]
                    item.item_price = products[choice]["price"]
                    item.item_quantity = int(input("Enter the item quantity:\n"))
                    cart.add_item(item)
                else:
                    print("Invalid product ID. Please choose a valid ID.")
            except ValueError:
                print("Please enter a number, not text.")

        # Remove item option (by cart index)
        elif option == "r":
            if not cart.cart_items:
                print("Your cart is empty. Nothing to remove.")
            else:
                print("Items in your cart:")
                for idx, item in enumerate(cart.cart_items, start=1):
                    print(f"{idx} - {item.item_name}")
                try:
                    remove_id = int(input("Enter the number of the item to remove:\n"))
                    if 1 <= remove_id <= len(cart.cart_items):
                        name = cart.cart_items[remove_id - 1].item_name
                        cart.remove_item(name)
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Please enter a valid number.")

        # Change quantity option (by cart index)
        elif option == "c":
            if not cart.cart_items:
                print("Your cart is empty. Nothing to modify.")
            else:
                print("Items in your cart:")
                for idx, item in enumerate(cart.cart_items, start=1):
                    print(f"{idx} - {item.item_name} (Current quantity: {item.item_quantity})")
                try:
                    modify_id = int(input("Enter the number of the item to modify:\n"))
                    if 1 <= modify_id <= len(cart.cart_items):
                        modified_item = ItemToPurchase()
                        modified_item.item_name = cart.cart_items[modify_id - 1].item_name
                        modified_item.item_quantity = int(input("Enter the new quantity:\n"))
                        cart.modify_item(modified_item)
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Please enter a valid number.")

        # Print descriptions option
        elif option == "i":
            cart.print_descriptions()

        # Print total option
        elif option == "o":
            cart.print_total()

        # Invalid option handling
        elif option != "q":
            print("Invalid option. Please choose again.")
# _____________________________________________________________
# Main Program
# ______________________________________________________________

# Adding the inputs of customers name and date is apart of Step 4 of the assignment.
def main():
    customer_name = input("Enter customer's name:\n").strip()
    current_date = datetime.now().strftime("%m/%d/%Y")
    cart = ShoppingCart()
    cart.customer_name = customer_name
    cart.current_date = current_date

    print_menu(cart)

if __name__ == "__main__":
    main()
# ================================
# End of Online Shopping Cart Program