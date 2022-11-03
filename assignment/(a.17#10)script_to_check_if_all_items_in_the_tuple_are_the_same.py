# script to check if all items in the tuple are the same.
t1 = (45, 45, 45, 45)
count = 0
for i in range(0, len(t1)):
    if t1[0] == t1[i]:
        count += 1
if count == len(t1):
    print("true")
