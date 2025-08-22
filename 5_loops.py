# For loops

for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

    # Can either print: 'number + j' to initalize or do 'range(1, n)'

# For Else

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Sucessful")
        break
else:
    print("Attempted 3 times and failed")

# Nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# Iterables

for y in "Python":  # Strings and lists are iterable like range
    print(y)

for z in [1, 2, 3, 4]:
    print(" ", z)

# While loops

numbera = 100
while numbera > 0:
    print(numbera)
    numbera //= 2

command = ""
# while command.lower() != "quit":
#    command = input(">")
#    print("ECHO", command)

# Infinite Loops

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break  # Always have break with loops like this
# same as the above while loop, just without initializing 'command'
