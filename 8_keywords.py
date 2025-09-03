# None

from typing import Any

data: Any = None
print(data)

# True

print(True + True)  # True is a constant for 1

# As

# rom random import randint as ri
# import math as m

# m.cos(10)
# ri(10, 20)

# Assert

db: str | None = 'message.db'
assert db, 'Cannot run the program withput the database.'

limit: int = 10
number: int = 2

assert number < limit, f'{number} is not less than the limit ({limit}).'

# Assertion enforces whatever condition you write after it. If the boolean condition fails, it will raise an assertion error, notifying you where the issue occurs.

#  Continue

names: list[str] = ['Tom', 'Bob', 'James']

for name in names:
    if name == 'Bob':
        print("We don't like you Bob")
        continue  # Ends the for loop right here and continues onto the next iteration

    print(f'Hello, {name}!')


# Del

new_name: str = "Bob"
print(new_name)

del new_name
# print(new_name)

# except (16)
