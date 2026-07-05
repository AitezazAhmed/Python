# Python doesn't require declaring the type
name = "Aitezaz"
age = 21
height = 5.9

print(name)
print(age)
print(height)

# How to find type of varibale
print(type(name))  # str
print(type(age))  # int
print(type(height))  # float

# Variable Naming Rules
name = "Ali"

my_name = "Ali"

age2 = 20

_name = "Ali"

################## Naming Conventions ###################

# Snake Case (Most Common)
first_name = "Ali"

total_marks = 90

#Camel Case

firstName = "Ali"

totalMarks = 90

# Pascal Case
FirstName = "Ali"

TotalMarks = 90

###########  Multiple Variables ############
  # One value to multiple variables
x = y = z = 100

print(x)

print(y)

print(z)

# Multiple values
name,age,city="Aitezaz",20,"Sargodha"
print(name)
print(type(name))
print(age)
print(type(age))
print(city)
print(type(city))

#  Reassigning Variables 

name = "Ali"

print(name)

name = "Ahmed"

print(name)

# Dynamic Typing
x = 10

print(type(x))

x = "Hello"

print(type(x))

# Variable Casting

age = "20"

age = int(age)
print(type(age))
print(age)


#  Variable Memory Address 

x = 10

print(id(x))

# . Delete Variable
x = 100

del x

# Global

x = 10

def change():
    global x
    x = 110   # now this changes the GLOBAL variable

change()
print(x)


####### Variable Swapping ########


a = 10

b = 20

a, b = b, a

print(a)

print(b)

####### Variable Swapping by using 3 varibales ######## 
a=10
b=20
c=0
c=a
a=b
b=c
print(a)
print(b)
