# Написать функцию, которая выбрасывает одно из трёх исключений:
# ValueError, TypeError или RuntimeError случайным образом.
# В месте вызова функции обрабатывать все три исключения.

import random

def raise_error():
    check = random.randint(1,3)
    if check == 1:
        raise ValueError('Wrong value!')
    elif check == 2:
        raise TypeError('Wrong type!')
    elif check == 3:
        raise RuntimeError('fuck!')

try:
    raise_error()
except ValueError as err:
    print('ValueError is raised!', err)
except TypeError as err:
    print('TypeError is raised!', err)
except RuntimeError as err:
    print('RuntimeError is raised!', err)




