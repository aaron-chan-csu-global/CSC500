# ------------------------------------------------
# 2/8/2025 Aaron Chan | CSC500 - Module 4 - Portfolio Milestone
# Script: csc500.module.4.portfolio.milestone.aaron.chan.py
# ------------------------------------------------
#
# Requirements (Online Shopping Cart)
# Step 1: Build the ItemToPurchase class with the following specifications:
# 
# Attributes
# item_name (string)
# item_price (float)
# item_quantity (int)
# Default constructor
# Initializes item's name = "none", item's price = 0, item's quantity = 0
# Method
# print_item_cost()
#
# ------------------------------------------------
# Modification Log:
# - 2/8/2025 Initiated.
# ------------------------------------------------

# ------------------------------------------------
# Method to obtain input from user related to a meal amount.
# ------------------------------------------------

from typing import Dict

class ItemToPurchase:
  # class constructor to initialize Item's Name, Item's Price and Item's Quantity, each with default value.
  def __init__(self, item_dictionary: Dict[str, object]):
    self.name: str = item_dictionary.get("item_name", "None")
    self.price: float = item_dictionary.get("item_price", 0)
    self.quantity: int = item_dictionary.get("item_quantity", 0)
    
  # Method to display the Item Name, Item Price, Item's Quantity of a given List, along with their Total Combined Purchase Price
  # The input list "items" is combined object instances of class ItemToPurchase, per each item
  def print_item_cost(items):
    print()

    # iterating through each item in the "items" List
    for i in items:
      # capturing variable representing current item's cost, which is the result of current item's price x quantity
      item_cost = float(i.price) * int(i.quantity)
      print(f"{i.name}\t{i.quantity} @ ${i.price} = ${item_cost:.2f}")

    # calculating and displaying the total combined purchase cost, of all ItemToPurchase object instances (as given in the "items" List
    total_purchase_cost = sum(float(i.price) * int(i.quantity) for i in items)
    print(f"\nTotal Cost = ${total_purchase_cost:.2f}")


# program main construct
if __name__ ==  '__main__':
  
  total_items_to_prompt = 2 # defining how many times the prompt will capture items. Initialized to 2.
  list_items = [] # empty List for purpose of capturing all instantiated ItemsToPurchase class objects

  # iterating through the total items to prompt, and invoke the prompt to capture information from the user
  for prompt in range(0, total_items_to_prompt):
    print() # printing an empty line to give some UI row spacing
    
    purchase_item_name = input("Enter the item name (e.g.: Apple): ")
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
    
    # apennd the object instance onto the List "list_items"
    list_items.append(obj_item)

  # invoking the class method print_item_cost() to display the individual items along with their total combined purchase cost
  ItemToPurchase.print_item_cost(list_items)
  
  
