

name ="Alia"
age = 20

formatted_string_oldstyle = " Hi my name is %s i am %d years old " %(name , age)
print (" Old Style : " + formatted_string_oldstyle)

formatted_string_format = "Hi my name is {} i am {} years old ".format(name,age)
print (" Str Formatting :  " + formatted_string_format)

formatted_string_fstring = f"Hi my name is {name} i am {age} years old "
print (" fStr Formatting :  " + formatted_string_fstring)