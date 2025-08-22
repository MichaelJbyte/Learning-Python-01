import math
x = 1
x = 1.1
x = 1 + 2j  # complex number

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)  # no exponent
print(10 % 3)  # remainder
print(10 ** 3)  # exponent

x = 10
x += 3

# Functions with Numbers

print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.2))

# Type Conversion

y = input("x: ")
print(type(y))  # identifies type of variable
z = int(y) + 1  # without int() func. results in syntax error.
# formatted str allows you to insert mult. variables into the string
print(f"x: {y}, y= {z}")

# Falsy: {"" , 0 , None} these variables return false

print(bool("False"))
