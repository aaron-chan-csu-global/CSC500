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
# Not In Scope:
# - This version focuses on demonstrating basic input capture, arithmatics (addition & substraction) and display, per assignment requirements,
#   and does not handle validation such as data types verification, etc.
#
# ------------------------------------------------
# Modification Log:
# - 1/16/2025 Initiated.
# - 1/19/2025 Add code comments.
# ------------------------------------------------


# ------------------------------------------------
# Input capture of variable num1 & num2 from End Users via command (e.g.: Shell command) prompt.
# ------------------------------------------------

num1 = input("\nEnter first number: ")
num2 = input("Enter second number: ")

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


