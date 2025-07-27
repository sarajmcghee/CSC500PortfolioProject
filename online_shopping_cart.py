class ItemToPurchase:
    def _init_(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
    def print_item_cost(self):
        total_cost = self.item_quantity * self.item_price
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

print("Item 1")
first_item = ItemToPurchase()
first_item.item_name = input("Enter the item name:\n")
first_item.item_price = float(input("Enter the item price:\n"))
first_item.item_quantity = int(input("Enter the item quantity:\n"))

print("\nItem 2")
second_item = ItemToPurchase()
second_item.item_name = input("Enter the item name:\n")
second_item.item_price = float(input("Enter the item price:\n"))
second_item.item_quantity = int(input("Enter the item quantity:\n"))

print("\nTOTAL COST")
first_item.print_item_cost()
second_item.print_item_cost()

total_cost = (first_item.item_quantity * first_item.item_price) + (second_item.item_quantity * second_item.item_price)

print(f"\nTotal: ${total_cost:.2f}")