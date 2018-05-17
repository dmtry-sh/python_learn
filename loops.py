print('# Infinitive loop: ')
while True:
    users_input = input('Please, input positive number: ')
    if float(users_input) > 0:
        print('Your number is: %s' % users_input)
        break
    else:
        print('%s is a wrong number.' % users_input)
        continue
