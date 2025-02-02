# ------------------------------------------------
# 2/2/2025 Aaron Chan | CSC500 - Module 3 - Critical Thinking Assignment - Part 2
# Script: csc500.module.3.critical.thinking.assignment.part.2.aaron.chan.py
# ------------------------------------------------
#
# Part 2 Requirements:
# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
# Write a Python program to solve the general version of the above problem.
# Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm.
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.
#
# ------------------------------------------------
# Modification Log:
# - 2/2/2025 Initiated.
# - 2/2/2025 Add code comments.
# ------------------------------------------------


# ------------------------------------------------
# Method to capture a current time in hours from end user.
# - input parameter 1: input_message_prompt. Expecting a message to be used for the input prompt, assigned with a default value.
# ------------------------------------------------
def get_current_time_in_hours(input_message_prompt = 'Enter a current time in hours.'):
    try:
        current_time_input_value = int(input(input_message_prompt))

        # catching invalid input range
        if current_time_input_value < 0 or current_time_input_value > 23:
            raise ValueError()

        return current_time_input_value
    except ValueError as ve:
        print(f"Invalid value. An integer value representing hour(s) between 0 (midnight) and 23 (11pm) is expected. {ve}")
        return None
    except Exception as e:
        print(f"Unexpected error has occured. {e}")
        return None

# ------------------------------------------------
# Method to capture a countdown value, representing the number of hours before the alarm is to go off.
# - input parameter 1: input_message_prompt. Expecting a message to be used for the input prompt, assigned with a default value.
# ------------------------------------------------
def get_countdown_to_alarm_in_hours(input_message_prompt = 'Enter a countdown value in hours before the alarm goes off'):
    try:
        countdown_to_alarm_input_value = int(input(input_message_prompt))

        # catching invalid input range
        if countdown_to_alarm_input_value < 0:
            raise ValueError()

        return countdown_to_alarm_input_value
    except ValueError as ve:
        print(f"Invalid countdown value. An integer value greater than or equal to 0 is expected. {ve}")
        return None
    except Exception as e:
        print(f"Unexpected error has occured. {e}")
        return None


# ------------------------------------------------
# Method to convert and return a 24-hour time to a 12-hour time with an AM/PM label.
# - input parameter 1: current_24hour_time, representing a 24-hour based time input value.
# ------------------------------------------------
def get_12hour_time_from_23hour_time(current_24hour_time):
    return str(
        12 if current_24hour_time == 0 
        else current_24hour_time if current_24hour_time <= 12 
        else current_24hour_time - 12
    ) + " "  + get_hour_am_pm_label(current_24hour_time)


# ------------------------------------------------
# Method to calculate and return the time (in 24-hours format) when the alarm is expected to go off, based on the input value of current time and countdown time provided by the user.
# - input parameter 1: input_message_prompt. Expecting a message to be used for the input prompt, assigned with a default value.
# ------------------------------------------------
def calculate_alarm_go_off_time(current_time, countdown_time):
    # get 12-hour time format for current time
    current_time_in_12hour_format = get_12hour_time_from_23hour_time(current_time)
    
    # Calculate alarm go-off time in both 24-hour and 12-hour format
    alarm_go_off_exact_time_in_24hour_format = (current_time + countdown_time) % 24
    alarm_go_off_exact_time_in_12hour_format = get_12hour_time_from_23hour_time(alarm_go_off_exact_time_in_24hour_format)


    countdown_days_and_time_to_elapse = str(countdown_time % 24) + " day(s) and " + str(countdown_time // 24) + " hour(s)"

    # Displaying all input info as well as the final calculated alarm setoff time.
    print("\nYou've entered:")
    print(f"\nCurrent time: {current_time_in_12hour_format}")
    print(f"Alarm countdown time: {countdown_time} hours")    
    print(f"\n\nThe alarm will go off in {countdown_days_and_time_to_elapse}, at {alarm_go_off_exact_time_in_12hour_format}.")

           


# ------------------------------------------------
# Method to determine the time label to use -- whether it's "AM" or "PM" -- based on the 24-hour input hours.
# - input parameter 1: hours_value, which represents a 24-hour input hour format.
# ------------------------------------------------
def get_hour_am_pm_label(hours_value):
    return "AM" if hours_value < 12 else "PM"



# ------------------------------------------------
# Method as program driver to capture needed information and direct other methods to perform sub tasks.
# ------------------------------------------------
def main():

    # ------------------------------------------------
    # Prompting user to current time in hours as well as the countdown value in hours to the alarm go-off time.
    # ------------------------------------------------

    current_time_in_hour = get_current_time_in_hours("\nEnter a current time in hour: ")

    if current_time_in_hour is None: # program stops (by-design) if user entered invalid current time value as determined by the method get_current_time_in_hours().
        print("\nProgram terminated.")
        return

    countdown_to_alarm_in_hour = get_countdown_to_alarm_in_hours("\nEnter a countdown to alarm time in hours: ")

    if countdown_to_alarm_in_hour is None: # program stops (by-design) if user entered invalid countdown time in hours value as determined by the method get_countdown_to_alarm_in_hours().
        print("\nProgram terminated.")
        return


    calculate_alarm_go_off_time(current_time_in_hour, countdown_to_alarm_in_hour)



# program main construct
if __name__ ==  '__main__': main()

