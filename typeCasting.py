'''
#Type of Type Casting in python
  1. Impecit Type Casting
  2. Explicit Type Casting
# Implicit Type Casting
  In this compiiler converts the data type automatically.
# Example:

'''
a = 7
print(type(a))
b = 3.0
print(type(b))
c = a + b
print(c)
print(type(c))
# Explicit Type Casting
  #In this we have to convert the data type manually.
# Example:
a = "1"
b = "2"
print(int(a) + int(b))
# Here we have to convert the string to integer
# Example:
string = "15"
number = 7
string_number = int(string)
sum = number + string_number
print("The sum of both the numbers is: ", sum)
# Here we have to convert the string to integer
# Example:
a = 7.0
print(type(a))
b = 3
print(type(b))
c = a + b
print(c)
print(type(c))
