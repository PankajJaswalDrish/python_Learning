#Input Function in python is used to take input from the user 
#it is taking input from the user in the form of string
#We can also take input from the user in the form of integer,float,complex,boolean etc.
#Example:
# a = input("Enter your name: ")
# print("My name is", a)
# x = input("Enter first number: ")
# y = input("Enter second number: ")

# print(x + y)#Here it added the two strings

# #Here we have to convert the string to integer
# print(int(x) + int(y))

'''
#Example: Creation of a calculator Using Input values from the user
'''

print("\t \t \t \t ------- Calculator Screen ------- ")
#Both a and b are of type int
a = input("Enter the Value of A : ")
Operator = input("Enter the operator: ")
b = input("Enter the Value of B: ")

print(a, Operator, b)

if Operator == "+":
  print("Addition of a and b  = ", int(a) + int(b))
elif Operator == "-":
  print("Subtraction of a and b  = ", int(a) - int(b))
elif Operator == "*":
  print("Multiplication of a and b  = ", int(a) * int(b))
elif Operator == "/":
  print("Devision of a and b  = ", int(a) / int(b))
elif Operator == "//":
  print("Floor of a and b is : ", int(a) // int(b))
elif Operator == "%":
  print("Modulus of a and b is : ", int(a) % int(b))
elif Operator == "**":
  print("Square operator of a and b is : ", int(a)**int(b))
