#Number divisible by another number

list_1 = [13, 14, 87, 44, 70, 9]

result = list (filter (lambda x: (x % 7 == 0), list_1))

print ("Numbers that are divisible by 7 are:", result)


