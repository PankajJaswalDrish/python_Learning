#String is used to store the textual data.
#String is a collection of characters is linke an array of characters. Which starts from the index[0].
# String is immutable.
#String in single as well as in double quotes.
#Example:
name = "Pankaj"
print("Hello", name)
print("Hello " + name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
# print(name[6])#This throws an error

st = ''' n a world tethered to our phones 24/7, where every need is met with a swipe or a tap, the constant allure of digital distractions has become an inescapable reality. Whether it's ordering food, indulging in a shopping spree across countless websites, or seeking entertainment in the form of endless reels and Candy Crush sessions—our phones have become our perpetual companions.'''

print(st)

st1 = """
Picture this: you wake up on a blissful holiday morning, greeted by a breathtaking view outside your window. Instinctively, you reach for your phone to capture the moment for the gram, only to realise it's nowhere in 
"""
print(st1)

# String Slicing
print("----String Slicing is used to access the elements of the string-----")
# Example:
name = "Pankaj"
print(name[0:6])
print(name[0:5])
print(name[0:4])
print(name[0:3])
print(name[0:2])
print(name[0:1])
print(name[0:0])
name1 = "ABCDEF"
print(name1[0:])
print(name1[:6])
print(name1[:5])
print(name1[:4])
print(name1[:3])
print(name1[:2])
print(name1[:1])
print(name1[:0])
print(name1[:])
name3 = "Harry"
print(name3[-4:-2])
print(name[-4:-3])
print(name1[-6:-2])#print(name1[Starting : ending - 1])

# String Methods
print("-----String Methods are used to modify the string-------")
# Example:
a = "Pankaj"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Pankaj", "John"))
print(a.split(" "))
blogHeading = "introduction to js"
print(blogHeading.capitalize())
str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Pankaj"))
print(str1.endswith("!!!"))
print(str1.endswith("to", 4, 10))
print(str1.find("to"))
print(str1.find("ishh"))
print(str1.index("to"))
# print(str1.index("ishh"))
str2 = "WelcomeToTheConsole"
print(str2.isalnum())
str3 = "Welcome"
print(str3.isalpha())
str4 = "hello world"
print(str4.islower())
str5 = "We wish you a Merry Christmas\n"
print(str5.isprintable())
str6 = "        "  #using Spacebar
print(str6.isspace())
str7 = "        "  #using Tab
print(str7.isspace())
str8 = "World Health Organization"
print(str8.istitle())
str9 = "To kill a Mocking bird"
print(str9.istitle())
str10 = "Python is a Interpreted Language"
print(str10.startswith("Python"))
print(str10.swapcase())
str11 = "His name is Dan. Dan is an honest man."
print(str11.title())
