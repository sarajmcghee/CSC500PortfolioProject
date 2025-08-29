class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "none"
    def print_item_cost(self):
        total_cost = self.item_quantity * self.item_price
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

class ShoppingCart:
        def __init__(self, customer_name = "none", current_date = "January 1, 2020"):
             self.customer_name = customer_name
             self.current_date  = current_date  
             self.cart_items = []

        def add_item(self, item_to_purchase):
             self.cart_items.append(item_to_purchase)

        def remove_item(self, item_name):
             for i, item in enumerate(self.cart_items):
                  if item.item_name == item_name:
                       self.cart_items.pop(i)
                       return
             print("Item not found in cart. Nothing removed.")    

        def modify_item(self, item_to_purchase):
             for  item in self.cart_items:
                  if item.item_name == item_to_purchase.item_name:
                       if item_to_purchase.item_description != "none":
                            item.item_description = item_to_purchase.item_description
                       if item_to_purchase.item_price != 0:
                            item.item_price = item_to_purchase.item_price
                       if item_to_purchase.item_quantity != 0: 
                            item.item_quantity = item_to_purchase.item_quantity
                       return
             print("Item not found in cart. Nothing modified.")    

        def get_num_items_in_cart(self):
             totalItems = sum(item.item_quantity for item in self.cart_items)
             return totalItems
        
        def get_cost_of_cart(self):
             totalCostofCart = sum((item.item_price * item.item_quantity)  for item in self.cart_items)
             return totalCostofCart
        
        def print_total(self):
             print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
             num_items = self.get_num_items_in_cart()
             print(f"Number of Items: {num_items}")
             if len(self.cart_items) == 0:
                  print("SHOPPING CART IS EMPTY")
                  print("Total: $0")
                  return
             
             for item in self.cart_items:
                 item.print_item_cost()
             print(f"Total: ${self.get_cost_of_cart()}")

        def print_descriptions(self):
             print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
             print("Item Descriptions")
             for item in self.cart_items:
                  print(f"{item.item_name}: {item.item_description}")


def print_menu(cart):
     menu = ( "MENU\n"
             "a - Add item to cart\n"
             "r - Remove item from cart\n"
             "c - Change item quantity\n"
             "i - Output items' descriptions\n"
             "o - Output shopping cart\n"
             "q - Quit\n"
             "Choose an option:\n")
     
     choice = "" 

     while choice != "q":
          print()
          print(menu)
          choice = input().strip().lower()

          match choice:
               case "a":
                    print("ADD ITEM TO CART")
                    item = ItemToPurchase()
                    item.item_name = input("Enter the item name:\n")
                    item.item_description = input("Enter the item's description:\n")
                    item.item_price = prompt_int("Enter the item price:\n")
                    item.item_quantity = prompt_int("Enter the item quantity:\n")
                    cart.add_item(item)

               case "r":
                    print("REMOVE ITEM FROM CART")
                    item_name = input("Enter name of item to remove:\n")
                    cart.remove_item(item_name)
               
               case "c":
                     print("CHANGE ITEM QUANTITY")
                     item = ItemToPurchase()
                     item.item_name = input("Enter the item name:\n")
                     item.item_quantity = prompt_int("Enter the quantity:\n")
                     cart.modify_item(item)
                
               case 'i':
                    print("OUTPUT ITEMS' DESCRIPTIONS")
                    cart.print_descriptions()

               case 'o':
                    print("OUTPUT SHOPPING CART")
                    cart.print_total()

               case 'q':
                    print("GOODBYE")
                    break
               case _:
                    print("Invalid option")

def prompt_int(input_text ):
     while True:
          number = input(input_text).strip()
          if number.isdigit():
               return int(number)
          else:
               print("Please enter a whole number")

def main():
     customer_name = input("Enter customer's name:\n")
     current_date = input("Enter today's date:\n")
     
     print(f"Customer's name: {current_date}")
     print(f"Today's date:  {current_date}")
     cart = ShoppingCart(customer_name, current_date)

     print_menu(cart)


if __name__ == "__main__":
     main()