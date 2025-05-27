# Creating and printing dictionaries
dic = {}
print(dic)

dic = {1: 'apple', 2: 'ball'}
print(dic)

dic = {'name': 3, 1: [2, 4, 3]}
print(dic)

myd = {'stuname': 'B', 'stuage': 20, 'stucity': 'cbe'}
print(myd)

# Adding a key-value pair
myd['sturegno'] = 2385005
print(myd)

# Accessing values
print(myd['stuname'], myd['stuage'], myd['stucity'], myd['sturegno'])

# Updating values
myd['stuage'] = 21
myd['stucity'] = 'Tpr'
print(myd)

# Looping through dictionary
for e in myd:
    print(e, myd[e])

# Deleting a key
del myd['stucity']
print(myd)

# Clearing dictionary
myd.clear()
print(myd)

# Deleting dictionary
del myd

# Copying a dictionary
dic1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
dic2 = dic1.copy()
print(dic2)

# Clearing a dictionary
dic1.clear()
print(dic1)

# Dictionary methods
print(dic2.get(1))
print(dic2.items())
print(dic2.keys())

# Removing elements
dic2.pop(4)
print(dic2)

dic2.popitem()
print(dic2)

# Updating dictionary
dic2.update({3: "Scala"})
print(dic2)

# Getting values
print(dic2.values())
