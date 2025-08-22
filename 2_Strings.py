# Python Fundamentals - Variables

students_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"

# print(students_count)

# Strings

course = "Python Programming"
message = """
Hi John, This is Michael practicing python...
"""

# print(len(message))
# print(course[-1])
# print(course[0:3])
# print(course[0:])
# print(course[:3])

# Escape Sequences    \"  \'  \\  \n

course_two = "Python \n\"Programming\""
# print(course_two)

# Formatted Strings

first = "Michael"
last = "Juarez"
full = f"{len(first)} {2 + 2}"
# can put any valid expression between curly brackets

# print(full)

# String Methods

course_three = ("   python programming")

print(course_three.upper())
print(course_three.title())
print(course_three.lstrip())
print(course_three.find("Pro"))  # returns index
print(course_three.replace("p", "j"))
print("pro" in course_three)  # returns boolean
print("pro" not in course_three)
