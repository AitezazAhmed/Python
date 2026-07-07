'''
10 → Integer
10.5 → Float
"Hello" → String
True → Boolean
'''

x = 10        # Integer
y = 10.5      # Float
name = "Ali"  # String

x = 10
print(type(x))



is_student = True
is_admin = False

print(type(is_student))



###############  List (list) ##############

numbers = [10, 20, 30]
# Ordered
#Changeable (Mutable)
#Allows duplicates
print(numbers)
numbers.append(40)
print(numbers)
print(type(numbers))
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)


########### Tuple (tuple) ##########
numbers = (10, 20, 30)

print(type(numbers))

#####  Set (set) #######

 # Unordered
 # No duplicate values
numbers = {10, 20, 30,20}
print(numbers)   #   Duplicates are automatically removed.
print(type(numbers))

##############  Dictionary (dict)###########

student = {
    "name": "Ali",
    "age": 20,
    "city": "Lahore"
}
print(student)
print(student["name"])     #  Access values
print(type(student))




