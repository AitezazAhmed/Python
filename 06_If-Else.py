

# ------------------------------------------------------------
# Example 1: Simple if
# ------------------------------------------------------------

print("Example 1")

age = 20

# Check if age is greater than or equal to 18
if age >= 18:
    print("You are an Adult.")

print()


# ------------------------------------------------------------
# Example 2: if False
# ------------------------------------------------------------

print("Example 2")

age = 15

# Condition is False, so nothing inside if will execute
if age >= 18:
    print("You are an Adult.")

print("Program Continues...")
print()


# ------------------------------------------------------------
# Example 3: if else
# ------------------------------------------------------------

print("Example 3")

age = 16

if age >= 18:
    print("You can Vote.")
else:
    print("You cannot Vote.")

print()


# ------------------------------------------------------------
# Example 4: Positive or Negative Number
# ------------------------------------------------------------

print("Example 4")

number = -5

if number > 0:
    print("Positive Number")
else:
    print("Negative Number")

print()


# ------------------------------------------------------------
# Example 5: Even or Odd
# ------------------------------------------------------------

print("Example 5")

num = 8

# Modulus (%) gives remainder
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print()


# ------------------------------------------------------------
# Example 6: if elif else
# ------------------------------------------------------------

print("Example 6")

marks = 82

if marks >= 90:
    print("Grade A")

elif marks >= 80:
    print("Grade B")

elif marks >= 70:
    print("Grade C")

elif marks >= 60:
    print("Grade D")

else:
    print("Fail")

print()


# ------------------------------------------------------------
# Example 7: Multiple Conditions using AND
# ------------------------------------------------------------

print("Example 7")

age = 22

if age >= 18 and age <= 30:
    print("Young Adult")
else:
    print("Not in Range")

print()


# ------------------------------------------------------------
# Example 8: Multiple Conditions using OR
# ------------------------------------------------------------

print("Example 8")

day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")

print()


# ------------------------------------------------------------
# Example 9: NOT Operator
# ------------------------------------------------------------

print("Example 9")

logged_in = False

if not logged_in:
    print("Please Login")
else:
    print("Welcome")

print()


# ------------------------------------------------------------
# Example 10: Nested if
# ------------------------------------------------------------

print("Example 10")

age = 25
citizen = True

if age >= 18:

    if citizen:
        print("Eligible to Vote")

    else:
        print("Not a Citizen")

else:
    print("Under Age")

print()


# ------------------------------------------------------------
# Example 11: Password Checker
# ------------------------------------------------------------

print("Example 11")

password = "python123"

if password == "python123":
    print("Login Successful")
else:
    print("Wrong Password")

print()


# ------------------------------------------------------------
# Example 12: Largest Number
# ------------------------------------------------------------

print("Example 12")

a = 20
b = 50

if a > b:
    print("A is Larger")
else:
    print("B is Larger")

print()


# ------------------------------------------------------------
# Example 13: Three Numbers
# ------------------------------------------------------------

print("Example 13")

a = 50
b = 70
c = 40

if a > b and a > c:
    print("A is Largest")

elif b > a and b > c:
    print("B is Largest")

else:
    print("C is Largest")

print()


# ------------------------------------------------------------
# Example 14: Character Check
# ------------------------------------------------------------

print("Example 14")

letter = "A"

if letter in "AEIOU":
    print("Vowel")
else:
    print("Consonant")

print()


# ------------------------------------------------------------
# Example 15: Number Check
# ------------------------------------------------------------

print("Example 15")

number = 0

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")

print()


# ------------------------------------------------------------
# Example 16: User Input
# ------------------------------------------------------------

print("Example 16")

age = int(input("Enter your age: "))

if age >= 18:
    print("You can Vote.")

else:
    print("You cannot Vote.")

print()


# ------------------------------------------------------------
# Example 17: Even/Odd using Input
# ------------------------------------------------------------

print("Example 17")

num = int(input("Enter a Number: "))

if num % 2 == 0:
    print("Even")

else:
    print("Odd")

print()


# ------------------------------------------------------------
# Example 18: Calculator
# ------------------------------------------------------------

print("Example 18")

num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

operation = input("Choose (+,-,*,/): ")

if operation == "+":
    print(num1 + num2)

elif operation == "-":
    print(num1 - num2)

elif operation == "*":
    print(num1 * num2)

elif operation == "/":
    print(num1 / num2)

else:
    print("Invalid Operator")

print()


# ------------------------------------------------------------
# Example 19: Login System
# ------------------------------------------------------------

print("Example 19")

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login Successful")

else:
    print("Invalid Username or Password")

print()


# ------------------------------------------------------------
# Example 20: Traffic Light
# ------------------------------------------------------------

print("Example 20")

color = input("Traffic Light (red/yellow/green): ")

if color == "red":
    print("STOP")

elif color == "yellow":
    print("READY")

elif color == "green":
    print("GO")

else:
    print("Invalid Color")

print()

