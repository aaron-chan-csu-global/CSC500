# ------------------------------------------------
# 2/1/2025 Aaron Chan | CSC500 - Module 3 - Critical Thinking Assignment - Part 1
# Script: csc500.module.3.critical.thinking.assignment.part.1.aaron.chan.py
# ------------------------------------------------
#
# Part 1 Requirements:
# Write a program that calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food and then calculate the amounts with an 18 percent tip and 7 percent sales tax.
# Display each of these amounts and the total price.
#
# ------------------------------------------------
# Modification Log:
# - 2/1/2025 Initiated.
# - 2/2/2025 Add code comments.
# ------------------------------------------------

# ------------------------------------------------
# Method to obtain input from user related to a meal amount.
# ------------------------------------------------
def get_meal_amount_input(input_message_prompt):
    try:
        meal_amount_input_value = float(input(input_message_prompt).replace('$', ''))
    
        if meal_amount_input_value <= 0: # additional rule: meal amount must be > 0
            raise ValueError("The meal amount must be greater than zero.")

        return meal_amount_input_value
    except ValueError as ve:
        print(f"Invalid value. A numeric value is expected. {ve}")
        return None
    except Exception as e:
        print(f"Unexpected error has occured. {e}")
        return None


# ------------------------------------------------
# Method to calculate and return tuple values of both tips amount and sales tax amount, based on the input values of meal_amount and the corresponding tips % and sales tax %
# ------------------------------------------------
def calculate_sales_tax_and_tips(meal_amount, tips_rate, sales_tax_rate):

    # calculate the tips amount based on multiple the meal amount with the tips rate
    calculated_tips = meal_amount * tips_rate

    # calculate the sales tax amount using formula of multiplying the pre-tipped meal amount with the sales tax rate
    calculated_sales_tax = meal_amount * sales_tax_rate

    # returning the tips and sales tax amount as tuple
    return (calculated_tips, calculated_sales_tax)

# ------------------------------------------------
# Method as program driver to capture needed information and direct other methods to perform sub tasks.
# two parameters configured with default values: default_tips = 0.18, default_sales_tax = 0.07
# ------------------------------------------------
def main(configured_tips = 0.18, configured_sales_tax = 0.07):

    # ------------------------------------------------
    # Prompting user to capture meal amount information.
    # ------------------------------------------------

    total_meal_amount = get_meal_amount_input("\nEnter the total amount purchased for your meal (e.g.: 123 or 123.45): ")

    if total_meal_amount is None: # program stops (by-design) if user entered invalid meal amount as determined by the method get_meal_amount_input().
        print("\nProgram terminated.")
        return


    # ------------------------------------------------
    # Determining the tips amount and sales amount leveraging the method get_tips_and_sales_tax_amount().
    # ------------------------------------------------

    # Obtaining the calculated tips and sales tax amount based on the meal amount and the configured tips and sales tax rate.
    calculated_sales_tax, calculated_tips = calculate_sales_tax_and_tips(total_meal_amount, configured_tips, configured_sales_tax)

    # Calculate total amount
    total_adjusted_meal_amount = total_meal_amount + calculated_sales_tax + calculated_tips

    print(f"Your Meal Amount: ${total_meal_amount:.2f}")
    print(f"\nYour Tips Amount (based on {configured_tips * 100:.2f}% tips rate): ${calculated_tips:.2f}")
    print(f"Your Sales Tax Amount (based on {configured_sales_tax * 100:.2f}% sales tax rate): ${calculated_sales_tax:.2f}")
    print(f"\nTotal Amount: ${total_meal_amount:.2f} + ${calculated_tips:.2f} + ${calculated_sales_tax:.2f} = ${total_adjusted_meal_amount:.2f}")

    print("\nProgram completed successfully.")

# program main construct
if __name__ ==  '__main__': main()

