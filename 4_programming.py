# Comparison Operators
print(10 >= 3)
print(10 != 3)
print(10 == "10")

print("bag" > "apple")  # follows alphabetical order to determine
print("bag" == "Bag")

# Condition Statements

temp = 15
if temp > 35:
    print("It's warm")
    print("Drink water")
elif temp > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

# Tenary Opertator

age = 10
# if age >= 18:
#    message = "Eligible"
# else:
#    message = "Not Eligible" | Same code but simplified v

message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

# Logical Operators

high_income = True
good_credit = True
student = True


if (high_income or good_credit) and not student:  # automatically compares; no need for == True
    print("Eligible")
else:
    print("Not Eligible")

# Chain Comparison Operators

age_2 = 22
if 18 <= age_2 < 65:  # | age_2 >= 18 and age < 65
    print("Eligible")
