# ------------------------------------------------
# 2/21/2025 Aaron Chan | CSC500 - Module 6 - Portfolio Milestone
# Script: csc500.module.6.portfolio.milestone.aaron.chan.py
# ------------------------------------------------
#
# Modification Log:
# - 2/21/2025 Initiated.
# ------------------------------------------------


from typing import Dict
from datetime import date, datetime
from typing import List, Any

# -----------------------------------------------------------------------------
# This class is a subset of Module 4 class implementation, and it is leveraged in this module alongside the newly created ShoppingCart class.
# -----------------------------------------------------------------------------
class ItemToPurchase:
  # class constructor to initialize Item's Name, Item's Price and Item's Quantity, each with default value.
  def __init__(self, item_dictionary: Dict[str, object] = {}) -> None:
    self.name: str = item_dictionary.get("item_name", "None")
    self.price: float = item_dictionary.get("item_price", 0)
    self.quantity: int = item_dictionary.get("item_quantity", 0)


# -----------------------------------------------------------------------------
# a ShoppingCart class
# -----------------------------------------------------------------------------
class ShoppingCart:
  
  __shopping_cart_is_empty_msg = "SHOPPING CART IS EMPTY" # a "private" string variable representing standard message indicating an empty shopping cart

  # -------------------------------------
  # a default class initializer, containing parameters with default values
  # -------------------------------------
  def __init__(self, cart_items: List[Any], customer_name = "none", current_date = "January 01, 2020") -> None:
    self.customer_name: str = customer_name
    self.current_date = current_date
    self.cart_items = cart_items

  # -------------------------------------
  # a method to add an item onto the shopping cart, along with its price and quantity info
  # if the item already exists in the cart, its quantity will be incremented accordingly
  # -------------------------------------
  def add_item(self, item_to_purchase: ItemToPurchase) -> None:

    # checking to see if item already exists in the cart -- if so, increment the quantity as needed, and exit the method.
    for i in self.cart_items:
      if i.name == item_to_purchase.name:
        i.quantity += item_to_purchase.quantity
        return # exit the add_item() method
    
    # this gets run only if there is net new item (by the item name)
    print(f"\nAdding {item_to_purchase.name} onto the cart...")
    self.cart_items.append(item_to_purchase)


  # -------------------------------------
  # a method to attempt to remove an item basd on its item name from the shopping cart, if exists
  # -------------------------------------
  def remove_item(self, item_name_to_remove: str) -> None:
    is_item_found_in_cart = False
    for i in self.cart_items:
      if i.name == item_name_to_remove:
        is_item_found_in_cart = True
        print(f"\nRemoving {item_name_to_remove} from the cart...")
        self.cart_items.remove(i)
        break


    if not is_item_found_in_cart:
      print("\nItem not found in cart. Nothing to be removed.")
  
  
  # -------------------------------------
  # a method to return the combined number of quantity of all items in the shopping cart.
  # -------------------------------------
  def get_num_items_in_cart(self) -> None:
    if self.cart_items:
      total_quantity = sum(int(i.quantity) for i in self.cart_items)
      print(f"\nThere are total of {total_quantity} item(s) in your cart.")

  # -------------------------------------
  # a method to attemp to calculate and display the combined overall cost of items in a shopping cart.
  # -------------------------------------
  def get_cost_of_cart(self) -> None:
    if self.cart_items:
      total_cost = sum(float(i.price) * int(i.quantity) for i in self.cart_items)
      print(f"\nTotal combined cost of items in the cart = ${total_cost:.2f}")

  # -------------------------------------
  # a method to display list of existing items in the cart, if any, along with its price, quantity and calculated cost info.
  # the method also leverage a separate method get_cost_of_cart() to display the calculated overall cost of the shopping cart.
  # -------------------------------------
  def print_total(self) -> None:
    if self.cart_items:
      print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
      print(f"\n\nNumber of Items: {len(self.cart_items)}")
      print("\n")
      for i in self.cart_items:
          item_cost = float(i.price) * int(i.quantity)
          print(f"\t{i.name}\t{i.quantity} @ ${i.price} = ${item_cost:.2f}")

      self.get_num_items_in_cart() # leveraging get_num_items_in_cart() display the total combined quantity of all items in the cart
      self.get_cost_of_cart() # leveraging get_cost_of_cart() display the total combined cost of all items in the cart
    else:
      print(f"\n{self.__shopping_cart_is_empty_msg}")

  # -------------------------------------
  # a method to display the list of item's name as in the shopping cart, if any.
  # -------------------------------------
  def print_descriptions(self) -> None:
    # Example of print_descriptions() output:
    # John Doe's Shopping Cart - February 1, 2020
    # Item Descriptions
    # Nike Romaleos: Volt color, Weightlifting shoes
    # Chocolate Chips: Semi-sweet
    # Powerbeats 2 Headphones: Bluetooth headphones
    if self.cart_items:
      print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
      print("\n\nItem Descriptions:")
      print("\n")
      for i in self.cart_items:
          print(f"\t{i.name}")
    else:
      print(f"\n{self.__shopping_cart_is_empty_msg}")


  # -------------------------------------
  # a method to capture necessary info from user for item they want removed, along with conditions to handle whether the item exsits (before attempting to remove)
  # -------------------------------------
  def modify_item(self, item_to_modify: ItemToPurchase) -> None:
    # if the attributes of item_to_modify input dictionary match default attributes of an ItemToPurchase constructor, do nothing
    if item_to_modify == ItemToPurchase():
      print("attributes match a default ItemToPurchase class constructor. Nothing is done.")
      return
    else:
      # the attributes of item_to_modify input dictionary do not match default attributes of an ItemToPurchase constructor

      is_item_to_remove_found_in_cart = False

      # attempting to modify the item, if found in the cart (based on item name)
      for i in self.cart_items:
        if i.name == item_to_modify.name:
          is_item_to_remove_found_in_cart = True

          print(f"\nUpdating {item_to_modify.name} info in the cart...")
          print("\nOld info:")
          print(f"\n\t{i.name}\t{i.quantity} @ ${i.price} = ${(int(i.quantity) * float(i.price)):.2f}")
          i.price = item_to_modify.price
          i.quantity = item_to_modify.quantity
          
          print("\nNew info:")
          print(f"\n\t{i.name}\t{i.quantity} @ ${i.price} = ${(int(i.quantity) * float(i.price)):.2f}")

          break # exit the for loop
      
      if not is_item_to_remove_found_in_cart:
        print("\nItem not found in cart. Nothing to be modified.")
    


# -------------------------------------
# a method leveraging menu-driven interactions with user to add, remove, modify, or display shopping items
# -------------------------------------
def print_menu(sc: ShoppingCart):
  while True:
    print("\n")
    print("--------------------------------")
    print("MENU")
    print("--------------------------------")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity or price")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print("--------------------------------")

    user_menu_option_choice = input("\nChoose an option (enter 'q' to quit): ")
    
    match user_menu_option_choice.lower():

      case 'q': # exiting the program. This case is prioritized by design over other input menu options.
        print("\nHave a nice day!")
        break

      case 'a': # capture basic info of item to add, and leverage add_item() method to add the item onto the shopping cart
        print() # printing an empty line to give some UI row spacing

        purchase_item_name = input("Enter the item name to add (e.g.: Apple): ")
        purchase_item_price = input("Enter the item price (e.g.: 2.99): ")
        purchase_item_quantity = input("Enter the item quantity (e.g.: 10): ")

        # creating a dictionary "item_data_dict"" capturing name, price and quantity of current item
        item_data_dict = {
          "item_name": purchase_item_name
          , "item_price": purchase_item_price
          , "item_quantity": purchase_item_quantity
        }

        # using the captured item dictionary, instantiate an object of class "ItemToPurchase"
        obj_item = ItemToPurchase(item_data_dict)
        sc.add_item(obj_item)

      case 'r': # leveraging remove_item() method to handle item removal request
        item_name_to_remove = input("Enter the item name to remove (e.g.: Apple): ")
        sc.remove_item(item_name_to_remove)

      case 'c': # capturing basic info of item to remove, and leverage modify_item() method to handle the shopping cart update
        print() # printing an empty line to give some UI row spacing

        purchase_item_name_to_modify = input("Enter the item name to modify (e.g.: Apple): ")
        purchase_item_price_to_modify = input("Enter the updated item price (e.g.: 2.99): ")
        purchase_item_quantity_to_modify = input("Enter the updated item quantity (e.g.: 10): ")

        # creating a dictionary "item_data_dict"" capturing name, price and quantity of current item
        item_data_dict_to_modify = {
          "item_name": purchase_item_name_to_modify
          , "item_price": purchase_item_price_to_modify
          , "item_quantity": purchase_item_quantity_to_modify
        }

        # using the captured item dictionary, instantiate an object of class "ItemToPurchase"
        obj_item_to_modify = ItemToPurchase(item_data_dict_to_modify)
        
        # leveraging modify_item() method in attempt to modify the cart info for item in question
        sc.modify_item(obj_item_to_modify)

      case 'i': # leveraging print_description() to display the list of item names as captured in the cart
        sc.print_descriptions()

      case 'o': # leveraging print_total() to display detail item price and quantity info, as captured in the cart along with the overall cost
        sc.print_total()

      case _: # a catch-all message for any menu option input that aren't recognized
        print("Not a valid option. Please try again.")
        

# -------------------------------------
# main construct as program main driver
# -------------------------------------
if __name__ ==  '__main__':

  # initializing a ShoppingCart class by providing some info
  sc = ShoppingCart(
    cart_items = []
    , customer_name = "Aaron"
    , current_date = date.today().strftime("%B %d, %Y")
  )
  
  # launching the shopping cart menu
  print_menu(sc)


