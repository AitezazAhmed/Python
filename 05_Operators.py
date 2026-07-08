# =====================================================
# 1. ARITHMETIC OPERATORS
# =====================================================

a = 10
b = 3

print("===== Arithmetic Operators =====")

# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", a - b)

# Multiplication
print("Multiplication:", a * b)

# Division (returns float)
print("Division:", a / b)

# Floor Division (removes decimal part)
print("Floor Division:", a // b)

# Modulus (returns remainder)
print("Modulus:", a % b)

# Exponent (Power)
print("Exponent:", a ** b)

print()


# =====================================================
# 2. ASSIGNMENT OPERATORS
# =====================================================

print("===== Assignment Operators =====")

x = 10
print("Initial Value:", x)

# x = x + 5
x += 5
print("After += :", x)

# x = x - 3
x -= 3
print("After -= :", x)

# x = x * 2
x *= 2
print("After *= :", x)

# x = x / 4
x /= 4
print("After /= :", x)

# x = x // 2
x //= 2
print("After //= :", x)

# x = x % 3
x %= 3
print("After %= :", x)

# x = x ** 2
x **= 2
print("After **= :", x)

print()


# =====================================================
# 3. COMPARISON OPERATORS
# =====================================================

print("===== Comparison Operators =====")

a = 10
b = 20

# Equal to
print("a == b :", a == b)

# Not equal
print("a != b :", a != b)

# Greater than
print("a > b :", a > b)

# Less than
print("a < b :", a < b)

# Greater than or equal
print("a >= b :", a >= b)

# Less than or equal
print("a <= b :", a <= b)

print()


# =====================================================
# 4. LOGICAL OPERATORS
# =====================================================

print("===== Logical Operators =====")

age = 22

# Both conditions must be True
print("AND :", age > 18 and age < 30)

# At least one condition should be True
print("OR :", age < 18 or age < 30)

# Reverse the result
print("NOT :", not(age > 18))

print()


# =====================================================
# 5. IDENTITY OPERATORS
# =====================================================

print("===== Identity Operators =====")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

# Same object?
print("list1 is list2 :", list1 is list2)

# Same values?
print("list1 == list3 :", list1 == list3)

# Same object?
print("list1 is list3 :", list1 is list3)

# Different object?
print("list1 is not list3 :", list1 is not list3)

print()


# =====================================================
# 6. MEMBERSHIP OPERATORS
# =====================================================

print("===== Membership Operators =====")

name = "Python"

# Check if character exists
print("'P' in name :", "P" in name)

# Check if character does not exist
print("'Z' not in name :", "Z" not in name)

numbers = [10, 20, 30, 40]

print("20 in numbers :", 20 in numbers)
print("100 in numbers :", 100 in numbers)

print()


# =====================================================
# 7. BITWISE OPERATORS
# =====================================================

print("===== Bitwise Operators =====")

a = 5
b = 3

# Binary AND
print("a & b :", a & b)

# Binary OR
print("a | b :", a | b)

# Binary XOR
print("a ^ b :", a ^ b)

# Binary NOT
print("~a :", ~a)

# Left Shift
print("a << 1 :", a << 1)

# Right Shift
print("a >> 1 :", a >> 1)

print()


# =====================================================
# 8. OPERATOR PRECEDENCE
# =====================================================

print("===== Operator Precedence =====")

# Multiplication happens first
print(2 + 3 * 4)

# Parentheses have highest priority
print((2 + 3) * 4)

print()


# =====================================================
# 9. PRACTICAL EXAMPLES
# =====================================================

print("===== Practical Examples =====")

num = 8

# Check Even/Odd
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

print()

age = 20

# Check Eligibility
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")

print()

marks = 85

# Grade Checker
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade D")

print()


# =====================================================
# 10. BONUS
# =====================================================

print("===== id() and type() =====")

x = 10

# Type of variable
print(type(x))

# Unique identity of object
print(id(x))

print()

