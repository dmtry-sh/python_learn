# Написать функцию, которая принимает на вход список. Если в списке все объекты - int,
# сортирует его. Иначе выбрасывает ValueError

def sort_int_list(l):
	for x in l:
		if type(x) != int:
			raise ValueError
	l.sort()
	return l
