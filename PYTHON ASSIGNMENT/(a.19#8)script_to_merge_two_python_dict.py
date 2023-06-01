# script to merge two python dict.
dict1 = {10: 'sk', 20: 'pk',  30: 'gk'}
dict2 = {40: 'sky', 50: 'pk', 60: 'pk'}
d = dict1.copy()
d.update(dict2)
print(d)
