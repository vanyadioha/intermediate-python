# Working with files in python
# file = open("file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Using the with keyword
# with open("file.txt") as file:
#     contents = file.read()
#     print(contents)

# Writing to a file
# mode 'w' deletes previous text before writing while mode 'a' simply adds the new text
with open("file.txt", mode="a") as file:
    file.write("\nHello people!")
