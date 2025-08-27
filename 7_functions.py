# Building Functions

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Thom", "Yorke")
print(greet("Johnny", "Greenwood"))

# Types of Functions

# 1- Perform a task | above ^
# 2- Return a value | below v


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Matt")  # not locked into printing

# Keyword Arguments


def increment(number, by):
    return number + by


print(increment(2, by=1))

# Optional Parameters


def increase(number, by=1):
    return number + by


print(increase(2, 5))

# xargs


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
