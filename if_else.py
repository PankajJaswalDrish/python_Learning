#Program To check Wheater a person is eligible to Drive or not
# a = int(input("Enter your Age : "))
# print("Entered Age is : ", a)
# if (a >= 18):
#   print("You are eligible to Drive")
# else:
#   print("You are not eligible to Drive")

# #Conditional Operators
# # <, >, <=, >=, ==, !=
# print(a>=18)
# print(a<=18)
# print(a==18)
# print(a!=18)


#Program to check Which is greater number 
a = int(input("Enter 1st Number = "))
b = int(input("Enter 2nd Number = "))
c = int(input("Enter 3rd Number = "))

# print("Entered 1st Number : ", a)
# print("Entered 2nd Number : ", b)
# print("Entered 3rd Number : ",c)
if (a>b and a>c):
  print("1st Number is Greater = ",a)
elif(b>a and b>c):
  print("2nd Number is Greater = ",b)
else:
  print("3rd Number is Greater = ",c)


z = 18
if (z>0):
  if(z>15):
    print("z is greater than 15")
  else:
    print("z is greater than 0 but not greater than 15")
elif(z==0):
  print("z is equal to 0")
elif(z<0):
  print("is negative")
else:
  print("z is 18")