# script to remove an item from a given set,if it is present in the set.
st = eval(input("enter a set:-"))
item = eval(input("enter an item which you want to remove:-"))
st.discard(item)
print(st)