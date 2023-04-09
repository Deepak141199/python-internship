#Sort dict by value
myDict = {'deepak': 10, 'neeraj': 9,
		'abhishek': 15, 'parag': 2, 'suraj': 32}

myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}

print(sorted_dict)
