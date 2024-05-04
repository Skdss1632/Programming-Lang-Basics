
# readlines

# with open ("python.txt", "r") as f:
#     lines = f.readlines() # it will return list of str
#     print(lines)

# writelines
with open("../gitlearning/LEETCODE SOLUTION/c.txt", "w") as f:
    lines = [" c is awesome", "\nc is my second fav programming language"]
    f.writelines(lines)