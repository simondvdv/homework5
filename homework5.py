immutable_var = (31, 'строка', ['спис', 0, 'к'], True)
print('\nЭлементы кортежа "immutable":', immutable_var)
try:
    immutable_var[0] = 200
except TypeError:
    print('immutable_var[0] =', immutable_var[0], ' \nКортеж - неизменяемый класс.'
                                                  'Можно было бы изменить элемент списка'
                                                  ' внутри кортежа, но сам элемент - нет'
                                                  '(так Денис в лекции сказал)\n')
mutable_list = [31, 'строка', ['спис', 0, 'к'], True]
mutable_list[0] = 'тридцать один'
print('Теперь вместо целого числа 31, у нас строка:', mutable_list[0])
