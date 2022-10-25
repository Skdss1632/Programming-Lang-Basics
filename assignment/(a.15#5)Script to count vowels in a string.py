# Script to count vowels in a string.

s = input("enter a string:-")
vowels = 'aeiouAEIOU'
count = 0
i = 0
while i < len(s):
	j = 0
	while j < len(vowels):
		if str[i:i+1] == vowels[j:j+1]:
			count += 1
			break
		j += 1
	i += 1
print("total no of vowels is:-", count)