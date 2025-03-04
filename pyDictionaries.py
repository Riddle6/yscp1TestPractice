print("\nPython Dictionaries")

myDict = {'name': 'David', 'age': 51, 'city': 'Norwood'}
myList = ['Python', 'Java', 'JS', 'C++', 'C#']

print("My name is: ", myDict['name'])
print("Language: ", myList[3])

print("\nAdding/Updating Items in a Dictionary\n")

myDict['country'] = 'USA'

myDict['age'] = 52

print(myDict)

myList.remove('JS')
print("\nLanguage: ", myList[3])

print("\nRemove Items from a dictionary\n")

del myDict['country']
print(myDict)

print("\nDelete an item from the Dictionary, and return it\'s value\n")

rem_value = myDict.pop('age')

print(rem_value)
print(myDict)

print("\nNew Dictionary\n")

Dict2 = {'fruits': ['apple orange mango banana grapes'.split()], 'vegetables': ['Broccoli', 'Brussel Sprouts', 'Carrots']}

# Add another fruit
Dict2['fruits'].append('cherry')

# Print the dictionary
print(Dict2)

print