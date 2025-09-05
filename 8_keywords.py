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

# Global

name: str = 'Bob'


def change_name():
    # tells python we are using the global varible, and not making a local var.
    global name

    name = 'James'


change_name()
print(name)

# Lambda (nameless function)

# A keyword you can use to replace a function,
# in the case you plan to only use it once.

# Nonlocal (like global, but for outer variables)


def func():
    item: str = 'candle'

    def inner_func():
        nonlocal item
        print(item)

    inner_func()


func()

# Pass (or ...)


def func_dos():
    pass

    # returns nothing, acts as placheholder

# Raise (literally raises an exception)

    # raise Exception('Manually raised an exception for no reason')


# With (allows you to open anc close files)

with open('text.txt', 'r') as file:
    text: str = file.read()
    print(text)

# Yield (used to make generators work)

    # from typing import Generator

    # def generate_num(limit: int):
    # for i in range(0, limit):
    # yield i

    # generated_nums: Generator = generate_num(10)
    # print(list(generated_nums))

# Match, Case, and _. (soft keyword, can be used as var. name)

weather_now: str = 'rain'

match weather_now:
    case 'rain':
        print('Not Again!')
    case 'cloudy':
        print('Aw Man.')
    case _:      # _ means: in any other case
        print('Unknown weather')
