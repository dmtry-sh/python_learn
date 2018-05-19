
# We can expand lists and dicts

def accepts_args(*args):
    print(args)
    return sum(args)

accepts_args(1, 3, 9, 0)

values = [1, 4, 9, 3]

try:
    accepts_args(values)
except TypeError as err:
    print('Error:', err)

accepts_args(*values)


# kwargs is the same

def accepts_kwargs(**kwargs):
    print(kwargs)

accepts_kwargs(name='Dima', job='dev')

values = {'day': 'wed', 'month': 'may'}

try:
    accepts_kwargs(values)
except TypeError as err:
    print('Error:', err)

accepts_kwargs(**values)

    
