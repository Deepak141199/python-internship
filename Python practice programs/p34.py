#getting last element of list
test_list = [1, 4, 5, 6, 3, 5]
print("The original list is : " + str(test_list))
for i in range(0, len(test_list)):

	if i == (len(test_list)-1):
		print("The last element of list using loop : "
			+ str(test_list[i]))


