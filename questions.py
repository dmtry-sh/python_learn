# game questions(ru) by Dmitry Shuklinov
# 23.04.2018


print('Игра: "Загадки"')
print('Правила: Отвечайте на вопросы.')
print('========================================================================')

print('Вопрос №1: ')
answer = input('Сколько будет 2*4? \n Ответ: ')
while int(answer) != 8:
    print('Это неправильный ответ!')
    answer = input('Введите ответ ещё раз: ')
    print()
print('Правильно!')
print()

print()
