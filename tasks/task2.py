# Написать функцию, которая принимает на вход список,
# если в списке все объекты - int, сортирует его.
# Иначе выбрасывает ValueError.

def sort_int_list(var_list):
    for x in var_list:
        if type(x) != int:
            raise ValueError('Wrong type!')
    var_list.sort()
    return var_list

sort_int_list([5,3,8,3,7,0,5,4,4])
sort_int_list([1,7,'2']) # выбросит ошибку 
