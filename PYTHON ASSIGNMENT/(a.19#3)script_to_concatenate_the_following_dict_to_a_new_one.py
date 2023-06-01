# script to concatenate the following dict to a new one.
# given dict
# dict1 = {1: 10, 2: 20}
# dict2 = {3: 30, 4: 40}
# dict3 = {5: 50, 6: 60}
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
new_dict = dict1.copy()
new_dict.update(dict2)
new_dict.update(dict3)
print(new_dict)