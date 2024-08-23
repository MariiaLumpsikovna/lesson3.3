def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(25,'Nosok')
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [False, 86, 'Merry Christmas']
values_dict = {'a': 'dog', 'b': 7, 'c': [4, 5, 6]}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3.4, 'Lumpsik']
print_params(*values_list_2)
