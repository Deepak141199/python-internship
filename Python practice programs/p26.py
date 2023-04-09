#Nested dict
Dict = { }
print("Initial nested dictionary:-")
print(Dict)

Dict['Dict1'] = {}
Dict['Dict1']['name'] = 'deepak'
Dict['Dict1']['age'] = 21
print("\nAfter adding dictionary Dict1")
print(Dict)

Dict['Dict2'] = {'name': 'Deeps', 'age': 23}
print("\nAfter adding dictionary Dict1")
print(Dict)
