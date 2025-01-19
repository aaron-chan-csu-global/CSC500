# ------------------------------------------------
# 1/16/2025 Aaron Chan | CSC500 - Module 1 - Critical Thinking Assignment | Creating Python Programs
# ------------------------------------------------
# CSC500 - Module 1 - Critical Thinking Assignment
#
# Creating Python Programs:
#
# Part 1 Requirements:
# Write a Python program to find the addition and subtraction of two numbers.
# Ask the user to input two numbers (num1 and num2). Given those two numbers, add them together to find the output.
# Also, subtract the two numbers to find the output.
#
# Part 2 Requirements:
# Write a Python program to find the multiplication and division of two numbers.
# Ask the user to input two numbers (num1 and num2). Given those two numbers, multiply them together to find the output.
# Also, divide num1/num2 to find the output.
#
# ------------------------------------------------
# Modification Log:
# - 1/16/2025 Initiated.
# - 1/19/2025 Add code comments.
# - 1/19/2025 Refactoring some codes to methods all part of modularization effort.
# ------------------------------------------------

# ------------------------------------------------
# Method to capture and return a number representing input from end users via command (e.g.: Shell command) prompt.
# ------------------------------------------------
def get_number_input(prompt_text):
    try:
        input_value = int(input(prompt_text))
    except ValueError:
        print("Invalid value. An integer is expected.")
    except Exception as e:
        print("Unexpected error has occured.")

    return input_value

# ------------------------------------------------
# Method containing the main program flows.
# ------------------------------------------------
def main():
    # ------------------------------------------------
    # Input capture of variable num1 & num2 handled by a separate method.
    # ------------------------------------------------

    num1 = get_number_input("\nEnter a number for num1: ")
    num2 = get_number_input("\nEnter a number for num2: ")

    # additional handling of num2, which must not be a zero (to prevent division by zero error)
    if num2 == 0:
        raise ValueError("num2 cannot be 0.") 

    # ------------------------------------------------
    # Displaying the captured input values.
    # ------------------------------------------------

    print("\nYou've entered num1 =", num1, ", num2 =", num2)


    # ------------------------------------------------
    # Displaying the output values, which also involves performing basic arithmatic operations to obtain the output values.
    # ------------------------------------------------

    print("\nThe sum of num1 and num2 is", num1, "+", num2, "=", int(num1) + int(num2))

    print("\nThe result of num1 minus num2 is", num1, "-", num2, "=", int(num1) - int(num2))

    print("\nThe result of num1 divided by num2 is", num1, "/", num2, "=", int(num1) / int(num2))


# program main construct
if __name__ ==  '__main__': main()

