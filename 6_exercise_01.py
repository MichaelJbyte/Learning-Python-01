# display even numbers from 1-10. After, print however many numbers were listed.
counter = 0
# for number in range(2, 10, 2):
#    print(number)
#    counter += 1
# print(f"We have {counter} even numbers")

count = 0
for number in range(1, 10):
    if (number % 2) != 1:
        print(number)
        count += 1
print(f"We have {count} even numbers")

# Answer

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
