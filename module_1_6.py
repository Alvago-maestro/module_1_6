my_dict = {'Ivan': 1980,
           'Roma': 1992,
           'Ira': 1993,
           'Dima': 1985}
print(my_dict)
print(my_dict['Dima'])
print(my_dict.get('Zina'))
my_dict.update(
    {'Koly': 1988,
    'Viktor': 1983})
a = my_dict.pop('Roma')
print(a)
print(my_dict)
my_set = {1, 3, 5, 8, 1, 3, 4, False, 'car'}
print(my_set)
my_set.update({7, 13})
my_set.discard(8)
print(my_set)
