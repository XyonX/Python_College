"""
Write a python code to access values stored in dictionary.
"""

student_list = {1: "Raj", 2: "Riya", 3: "Rohan", 4: "Mira"}


def access_student ( student_roll):
    return student_list[student_roll]

roll = int(input ("Enter the student Roll Num :"))

print( f"Name of the student of Roll {roll} is { student_list[roll]}")

"""
C:\Projects\College\Python\venv\Scripts\python.exe C:/Projects/College/Python/Assignment/7.py
Enter the student Roll Num :4
Name of the student of Roll 4 is Mira

Process finished with exit code 0

"""