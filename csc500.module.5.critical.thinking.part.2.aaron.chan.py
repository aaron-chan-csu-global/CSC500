# ------------------------------------------------
# 2/15/2025 Aaron Chan | CSC500 - Module 5 - Critical Thinking Assignment - Part 2 of 2
# Script: csc500.module.5.critical.thinking.part.2.aaron.chan.py
# ------------------------------------------------
#
# Requirements:
# The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. The points are awarded as follows:
#
# If a customer purchases 0 books, they earn 0 points.
# If a customer purchases 2 books, they earn 5 points.
# If a customer purchases 4 books, they earn 15 points.
# If a customer purchases 6 books, they earn 30 points.
# If a customer purchases 8 or more books, they earn 60 points.
#
# Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.
#
# ------------------------------------------------
# Modification Log:
# - 2/15/2025 Initiated.
# ------------------------------------------------

from typing import Dict

# Method to calculate and display the total award points for the user based on the number of books purchased
def get_award_points_by_book_purchase(no_of_books_purchased):
  # a dictionary based award point "configuration", consisted of key-value pair of the key (minimum threshold of # of book purchased) and value (the qualified award point "tier")
  dict_purchase_threshold_and_award_points = {8 : 60, 6 : 30, 4 : 15,  2 : 5, 0 : 0}

  # initializing the final award point as zero
  final_award_point = 0

  # iterating through the book purchase threshold and award point configuration to determine appropriate award point based on the user's number of book purchases
  for book_count_threshold, award_points in dict_purchase_threshold_and_award_points.items():
    if (no_of_books_purchased >= book_count_threshold):
      final_award_point = award_points
      break

  # displaying the final award points based on the book purchase info
  print(f"\nYou've purchased {no_of_books_purchased} book(s).")
  print(f"Your are awarded with {final_award_point} point(s).")
  

# program main construct
if __name__ ==  '__main__':

  # prompting and capturing from the user the number of books purchase this month
  number_of_books_purchased = input("Enter the number of books purchased this month (e.g.: 3 for 3 books): ") or 0 # defaulted to zero book using short-circuit evaluation

  # verifying that the number of years is a valid positive digit
  if (not str(number_of_books_purchased).isdigit() or int(number_of_books_purchased) < 0):
    print(f"The input \"number of books\" cannot be a negative value. You've entered \"{number_of_books_purchased}\".")
    print("\nProgram terminated.") # terminating the program by-design
  else:
    # leveraging the method to determine the award points based on the number of books purchased
    get_award_points_by_book_purchase(int(number_of_books_purchased))



