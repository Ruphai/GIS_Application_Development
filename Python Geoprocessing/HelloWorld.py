#Purpose: Introductory Python for Geoprocessing
#Author: Rufai Omowunmi Balogun
#Date of Creation:
#from datetime import date
#now = date.today()
#print("Hello world, today is: " + str(now))

#import arcpy, os
#arcpy,BufferError

a = 5
print(a)

b = 5 + 6
print(b)

c = "Hello"
d = ['Hello', 'Python', 'Lists', 'Variables']

print(c)
print(d[0])
print(d[2])
print(d[3])
print(d[-1])

#Python is case sensitive.

#String Concatenation
name = 'Streets'
types = '.shp'
print(name + types)

i = 1

print (name + str(i) + types)

e = 2.645
f = round(e, 1)
print(f)


strVariable = "5020"
intVariable = int(strVariable)
print (intVariable *2)

# Methods are like functions, except that they are associated with a particular
# object

IstVariable = [1, 2, 3, 4, 5, 6, 7]
print(IstVariable)

IstVariable.append(8) #.append is a method of the list variable type.

print(IstVariable)

#String also have specific methods:::
strVariable = "c:\\temp \\Data"
print (strVariable.find(":"))
newVariable = strVariable.replace("c:", "d:") #keep in mind that the replace
#method does not just replace the first character in the string but all
#occurences of the character in the string.
print (newVariable)

#In contrasts the methods of lists and dictionaries, strings are immutable.
#the results of the methods have to be saved in a  new variable.


#Interactive input.
userVariable = input("Select a file name:")
print ("The selected file name is : " + userVariable)

# The input variable stored values as strings.
# If you want to collect numbers, you have to typecast them.
userVariable = input("Please enter a number:")
numCalc = float(userVariable)*float(userVariable)
print (numCalc)