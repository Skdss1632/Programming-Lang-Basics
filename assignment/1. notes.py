# using (and) in if statement
strs = ['flower', 'flow', 'flight']
s2 = strs[0][0]
if s2 in strs[1] and s2 in strs[2]:
    print(s2)
else:
    print('no')