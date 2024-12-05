#The filter() function returns an iterator that only contains the elements for which the condition is True.
num_list = [10,501,22,37,100,999,87,351]
#filter(): function to filter out the elements and an iterable
result = filter(lambda x: x > 4, num_list)
#The lambda function lambda x: x > 4 checks if each element in num_list is greater than 4
print(list(result))
#output: [10, 501, 22, 37, 100, 999, 87, 351]
