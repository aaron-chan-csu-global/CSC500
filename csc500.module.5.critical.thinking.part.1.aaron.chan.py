# ------------------------------------------------
# 2/15/2025 Aaron Chan | CSC500 - Module 5 - Critical Thinking Assignment - Part 1 of 2
# Script: csc500.module.5.critical.thinking.part.1.aaron.chan.py
# ------------------------------------------------
#
# Requirements:
# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year. The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
# After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.
#
# ------------------------------------------------
# Modification Log:
# - 2/15/2025 Initiated.
# ------------------------------------------------

from typing import Dict

# Method to prompt user and capture rainfall data for individual months for a specified duration of years
# input parameters: no_of_years: an integer representing the number of years
def capture_rainfall_data(no_of_years):

  list_inches_of_rain = [] # list to capture monthly rain data

  for y in range(no_of_years): # outer for loop, interating the number of years (no_of_years) input parameter
    for m in range(12): # inner for loop, iterating over each of the 12 months in the given year
      try:
          # prompt to capture the amount of rain.
          current_month_rainfall = float(input(f"Enter inches of rainfall for Month {(m + 1):02} of Year {y + 1}: ")) or 0

          if not isinstance(current_month_rainfall, (int, float)) or float(current_month_rainfall) < 0:
            raise ValueError("Invalid rainfall value. Expects a non-negative number.")
      except ValueError: # catch-
        print(f"A default value of 0 is used for Year {y + 1} and Month {(m + 1):02}.")
        current_month_rainfall = 0

      list_inches_of_rain.append(current_month_rainfall)

  return list_inches_of_rain # returning captured rainfall dta to the caller


# Method to display summary of rainfall data.
# The summary includes average month rainfall for the duration of data provided.
def get_rainfall_summary(list_monthly_rainfall_data):
  # verify if there is rainfall data before proceeding with calculating and displaying the summary rainfall information.
  if (len(list_monthly_rainfall_data) > 0):
    total_rainfall = sum(list_monthly_rainfall_data)
    total_months = len(list_monthly_rainfall_data)
  
    print(f"\nTotal inches of rainfall captured for the duration of {len(list_monthly_rainfall_data):0d} month(s) = {total_rainfall:.2f}")
    print(f"\nAverage monthly inches of rainfall {(total_rainfall / total_months):02f}.")
  else:
    print("No rainfall data observed.")

# program main construct
if __name__ ==  '__main__':

  number_of_years = input("Enter the number of years (e.g.: 2 for 2 year(s)): ") # prompting and capturing the number of years from the user

  # verifying that the number of years is a valid positive digit
  if (not str(number_of_years).isdigit() or int(number_of_years) < 1):
    print(f"The input \"number of years\" expects a positive integer value. You've entered \"{number_of_years}\".")
    print("\nProgram terminated.") # terminating the program by-design

  # leveraging the method to capture monthly rainfall data from user
  list_rainfall_data = capture_rainfall_data(int(number_of_years))

  # leveraging the method to calculate and display summary rainfall result
  get_rainfall_summary(list_rainfall_data)


