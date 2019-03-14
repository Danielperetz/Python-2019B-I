name="Bob and Alice"


# startswith = Return True if the string starts with the specified prefix,False otherwise
print("name.startswith(\"Bo\")")
print(name.startswith("Bo"))
print("------------------------")


print("name.startswith(\"Alice\")")
print(name.startswith("Alice"))
print("------------------------")


# endswith = Return True if the string ends with the specified suffix, False otherwise
print("name.endswith(\"Alice\")")
print(name.endswith("Alice"))
print("------------------------")


# in = checks if the string in the left side is contained in the right side
print("\"or\" in name")
print("or" in name)
print("------------------------")

print("\"and\" in name")
print("and" in name)
print("------------------------")


# will print the char in index 2 (the third char)
print("name[2]")
print(name[2])
print("------------------------")



"""
Example 1 of program execution:
___________________________________


name.startswith("Bo")
True
------------------------
name.startswith("Alice")
False
------------------------
name.endswith("Alice")
True
------------------------
"or" in name
False
------------------------
"and" in name
True
------------------------
name[2]
b
------------------------
"""

