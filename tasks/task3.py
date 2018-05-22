# Написать функцию, которая принимает словарь,
# преобразует все ключи словаря к строкам и возвращает новый словарь.

def keys_to_str(this_dict):
    new_dict = {}
    for key, value in this_dict.items():
        new_dict.update({str(key): value})
    return new_dict

keys_to_str({1: 'x1', 2: 'x2', 3: 'x3'})
    
    
