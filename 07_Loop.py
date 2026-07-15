# Loops are used to repeat code.

# There are two loops in Python:
# 1. for loop
# 2. while loop

# ==========================================================
# FOR LOOP
# ==========================================================

print("========== FOR LOOP ==========")

# Example 1
# Print numbers from 1 to 5

for i in range(1, 6):
    print(i)

print()

# ==========================================================

# Example 2
# Print numbers from 1 to 10

for i in range(1, 11):
    print(i)

print()

# ==========================================================

# Example 3
# Print even numbers

for i in range(2, 11, 2):
    print(i)

print()

# ==========================================================

# Example 4
# Print odd numbers

for i in range(1, 10, 2):
    print(i)

print()

# ==========================================================

# Example 5
# Print numbers in reverse

for i in range(10, 0, -1):
    print(i)

print()

# ==========================================================

# Example 6
# Print a string

name = "Python"

for letter in name:
    print(letter)

print()

# ==========================================================

# Example 7
# Loop through a list

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

print()

# ==========================================================

# Example 8
# Sum of numbers

total = 0

for i in range(1, 6):
    total += i

print("Sum =", total)

print()

# ==========================================================

# Example 9
# Multiplication table

number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

print()

# ==========================================================

# Example 10
# Print stars

for i in range(5):
    print("*")

print()

# ==========================================================
# NESTED FOR LOOP
# ==========================================================

print("========== NESTED FOR LOOP ==========")

# Example 11

for i in range(3):
    for j in range(3):
        print(i, j)

print()

# ==========================================================

# Example 12
# Square pattern

for i in range(5):
    print("* " * 5)

print()

# ==========================================================

# Example 13
# Triangle

for i in range(1, 6):
    print("*" * i)

print()

# ==========================================================

# Example 14
# Reverse Triangle

for i in range(5, 0, -1):
    print("*" * i)

print()

# ==========================================================
# WHILE LOOP
# ==========================================================

print("========== WHILE LOOP ==========")

# Example 15

i = 1

while i <= 5:
    print(i)
    i += 1

print()

# ==========================================================

# Example 16

i = 10

while i >= 1:
    print(i)
    i -= 1

print()

# ==========================================================

# Example 17
# Even numbers

i = 2

while i <= 10:
    print(i)
    i += 2

print()

# ==========================================================

# Example 18
# Odd numbers

i = 1

while i <= 9:
    print(i)
    i += 2

print()

# ==========================================================
# break
# ==========================================================

print("========== BREAK ==========")

for i in range(1, 11):

    if i == 6:
        break

    print(i)

print()

# ==========================================================
# continue
# ==========================================================

print("========== CONTINUE ==========")

for i in range(1, 11):

    if i == 6:
        continue

    print(i)

print()

# ==========================================================
# pass
# ==========================================================

print("========== PASS ==========")

for i in range(5):

    if i == 3:
        pass

    print(i)

print()

# ==========================================================
# INPUT EXAMPLES
# ==========================================================

print("========== USER INPUT ==========")

# Example 19

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

print()

# ==========================================================

# Example 20
# Sum from 1 to N

n = int(input("Enter N: "))

sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum =", sum)

print()

# ==========================================================

# Example 21
# Factorial

num = int(input("Enter Number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)

print()

# ==========================================================

# Example 22
# Count Down

count = 5

while count > 0:
    print(count)
    count -= 1

print("Blast Off!")

print()

# ==========================================================

# Example 23
# Guess Loop

password = ""

while password != "python":
    password = input("Enter Password: ")

print("Access Granted")

print()

# ==========================================================

# Example 24
# Find Even Numbers

for i in range(1, 21):

    if i % 2 == 0:
        print(i)

print()

# ==========================================================

# Example 25
# Find Odd Numbers

for i in range(1, 21):

    if i % 2 != 0:
        print(i)

print()

# ==========================================================
# enumerate()
# ==========================================================

print("========== ENUMERATE ==========")

colors = ["Red", "Green", "Blue"]

for index, color in enumerate(colors):
    print(index, color)

print()

# ==========================================================
# zip()
# ==========================================================

print("========== ZIP ==========")

names = ["Ali", "Ahmed", "Sara"]
marks = [80, 90, 95]

for n, m in zip(names, marks):
    print(n, m)

print()

# ==========================================================
# else with loop
# ==========================================================

print("========== LOOP ELSE ==========")

for i in range(5):
    print(i)
else:
    print("Loop Finished")

print()

# ==========================================================
# Infinite Loop Example (Commented)
# ==========================================================

# while True:
#     print("Infinite Loop")