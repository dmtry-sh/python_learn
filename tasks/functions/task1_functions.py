# Игра "Угадай число"
import random

print('Игра "Угадай число"')
print('Вам нужно угадать число от 0 до 100, загаданное компьютером.')
print('Если вы не угадали число за 10 попыток, вы проигрываете.')
print('Число загадано.')

life = 10
random_digit = random.randint(1,99)
print(random_digit)

print('Введите число:', end = '')
try:  
    user_digit = int(input())
except:
    while type(user_digit) != int:
        print('Введите число:', end = ' ')
        try:
            user_digit = int(input())
        except:
            pass
if user_digit == random_digit:
    print('Вы выиграли!')
else:
    if random_digit - 5 <= user_digit <= random_digit + 5 and random_digit != user_digit:
            print('Горячо')
    life -= 1
    print('У вас осталось', life, 'попыток.')

    while random_digit != user_digit or life != 0:
        print('Введите число:', end = ' ')
        try:
            user_digit = int(input())
        except:
            while type(user_digit) != int:
                print('Введите число:', end = '')
                try:
                    user_digit = int(input())
                except:
                    pass

        if random_digit - 5 <= user_digit <= random_digit + 5 and random_digit != user_digit:
            print('Горячо')

        life -= 1
        print('У вас осталось', life, 'попыток.')
    
    print('Вы проиграли.')
	

