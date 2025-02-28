# ------------------------------------------------
# 2/27/2025 Aaron Chan | CSC500 - Module 7 - Critical Thinking Assignment
# Script: csc500.module.7.critical.thinking.aaron.chan.py
# ------------------------------------------------
#
# ------------------------------------------------
# Modification Log:
# - 2/27/2025 Initiated.
# ------------------------------------------------

from typing import Dict

# program main construct
if __name__ ==  '__main__':
  
  # dictionary object containing course room numbers per each course
  dict_room_number = {
    "CSC101": 3004
    , "CSC102": 4501
    , "CSC103": 6755
    , "NET110": 1244
    , "COM241": 1411
  }

  # dictionary object containing course instructor name per each course
  dict_instructor = {
    "CSC101": "Haynes"
    , "CSC102": "Alvarado"
    , "CSC103": "Rich"
    , "NET110": "Burke"
    , "COM241": "Lee"
  }
  
  # dictionary object containing course meeting time per each course
  dict_meeting_time = {
    "CSC101": "8:00 a.m."
    , "CSC102": "9:00 a.m."
    , "CSC103": "10:00 a.m."
    , "NET110": "11:00 a.m."
    , "COM241": "1:00 p.m."
  }
    
  
  # prompting and capturing from the user the course number
  course_number = input("Enter the course number (e.g.: CSC101): ").upper()

  # imposing that the course must exist in all three dictionary objects
  if course_number in dict_room_number and course_number in dict_room_number and course_number in dict_meeting_time:
    print(f"\nCourse Info for {course_number}:\n")
    print(f"\tRoom Number: {dict_room_number[course_number]}")
    print(f"\tInstructor: {dict_instructor[course_number]}")
    print(f"\tMeeting Time: {dict_meeting_time[course_number]}")
  else:
    print(f"Course info not found for {course_number}.")

