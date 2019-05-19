word = 'geeks for geeksz'

# returns first occurrence of Substring
result = word.find('geeks')
print ("Substring 'geeks' found at index:", result )

result = word.find('for')
print ("Substring 'for ' found at index:", result )

# How to use find()
if (word.find('pawan') != -1):
	print ("Contains given substring ")
else:
	print ("Doesn't contains given substring")
result = word.find('z')
print ("T: " , result)
print ("===================================================")
#//////////////////


word = 'geeks for geeks'

# Substring is searched in 'eks for geeks'
#tim tu vi tri thu 2 cua cau

print(word.find('ge', 2))

# Substring is searched in 'eks for geeks'
print(word.find('geeks', 2))

# Substring is searched in 's for g'
print(word.find('g', 4, 10))

# Substring is searched in 's for g'
print(word.find('for ', 4, 11))


