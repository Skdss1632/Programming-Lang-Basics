# script to combine two dict adding values for common keys.
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 200, 'c': 400, 'e': 300}
for k in dict1:
    if k in dict2:
        dict2[k] = dict1[k] + dict2[k]
    else:
        dict2[k] = dict1[k]
print(dict2)