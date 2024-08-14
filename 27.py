
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Item(name={self.name}, price={self.price})"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} added to the cart.")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"{item.name} removed from the cart.")
                break
        else:
            print(f"Item with name {item_name} not found in the cart.")

    def display_items(self):
        if not self.items:
            print("The shopping cart is empty.")
        else:
            print("Items in the shopping cart:")
            for item in self.items:
                print(f" - {item.name}: ${item.price}")

# Example usage:
if __name__ == "__main__":
    cart = ShoppingCart()
    item1 = Item("Apple", 0.99)
    item2 = Item("Banana", 0.59)
    cart.add_item(item1)
    cart.add_item(item2)
    cart.display_items()
    cart.remove_item("Apple")
    cart.display_items()
    cart.remove_item("Orange")


