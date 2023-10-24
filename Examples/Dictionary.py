

#Declaration of a  empty dictionary

empty_dict = {}

student_list = {1: "Raj", 2: "Riya", 3: "Rohan", 4: "Mira"}


student_roll = 4

#Accessing Value
student_name = student_list[student_roll]
#print(f"student Roll :  {student_roll} is : {student_name}")

#Modifying Values:
new_student = "Shyam"
student_list[1] = new_student

#Adding New Key-Value Pairs
student_list[5] = "Rahul"


print(student_list)


# Removing Key-Value Pairs
del student_list[5]

print(student_list)


