# When dealing with mixed data types in a list,
# isinstance() can be used to filter elements based on their type.
# For example, to separate integers and strings from a list.
data = ['apple', 3, 'banana', 2, 'cherry']
find_integers = filter(lambda x: isinstance(x,int), data)
find_strings = filter(lambda x: isinstance(x,str), data)
print(list(find_integers))
print(list(find_strings))