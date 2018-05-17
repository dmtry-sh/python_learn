# Написать функцию, которая принимает список чисел
# и возвращает их произведение.

def multiply_list_elements(var_list):
    p = 1
    for x in var_list:
        p *= x
    return p

p = multiply_list_elements([1, 2, 4, 7, 7, 7])
