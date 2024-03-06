# I can concating the string using the + operation.

# lets take three parameter

name = "Bikram Mahato"
year = "21"
degree = "BCS"
unique_number = "9491"
Full_UID = name + ":" + year + degree + unique_number
print(Full_UID)

# += method in string concating

exp = "Its"
exp += " very"
exp += " worm"
exp += " day"

print(exp)

# Example fo f string

age = 100
info = f"My age is {age}"
print(info) 

# Use the format method:

Laptop = "lenovo_LOQ"
Gpu = "Gforce RTX 4060"
desc = "brand is {} and Gpu is {}".format(Laptop, Gpu)
print(desc)

# Join method in python concatination

details = ["My", "Height", "is","6 " "feet"]
sentence = " ".join(details)
print(sentence)

# Number joining string concating:

numbers = ["1", "2", "3", "4"]
csv_string = ",".join(numbers)
print(csv_string)



