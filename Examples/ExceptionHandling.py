

try:
    uservalue_str = input ("Type the value : ")
    uservalue_int = int(uservalue_str)
    print("Succssfull Converted to int : " , uservalue_int)

except ValueError:
    print("Invalid Input . Please  eter a valid Integer")