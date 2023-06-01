# reading file in python

# f = open(r"C:\Users\91707\OneDrive\Documents\s.txt.txt", "r")
# content = f.read(2)
# print(content)
#
# more_content = f.read(7)
# print(more_content)
#
# f.close()




# reading file in python

# if i don't want to use exception handling file in python then i can use with open and it automatically close the file
# with open (r"C:\Users\91707\OneDrive\Documents\s.txt.txt", "r") as f:
#     content = f.read(2)
#     print(content)
#
#     more_content = f.read(7)
#     print(more_content)

# writing file:- if a file doesn't exist, a new file is created.. if the file already exist,it's overwritten

# with open ("python.txt", "w") as f:
#     f.write("python is awesome\n")
#     f.write("fjgjkfje")

# appending to files

# with open ("python.txt", "a") as f:
#     f.write("\npython is my fav programming language")

# readlines

# with open ("python.txt", "r") as f:
#     lines = f.readlines() # it will return list of str
#     print(lines)

# writelines
with open("../leetcodeSolution/c.txt", "w") as f:
    lines = [" c is awesome", "\nc is my second fav programming language"]
    f.writelines(lines)



