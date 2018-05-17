# Step 0:

# Here we define a function:
def this_function_prints_stars():
	print('I will print stars!')
	print('**********')

# Here we call the function:
this_function_prints_stars()


# Step 1:

def my_function(input_var1, input_var2):
	print(input_var1, input_var2)
	return input_var1 + input_var2

first_call = my_function(1, 1)
print(first_call)

second_call = my_function(1, 123)
print(second_call)




# Step 2:
def my_function(var1, var2, var3):
	print("No way I'm using this: {}, {}, {}".format(var1, var2, var3))

# my_function now is redefined to accept 3 arguments: 
new_call = my_function(1, 2, 3)
print(new_call) 




# Step 3:
def function_with_default_value(name, age=0, needs_stars=False):
	message = '{} is {} years old!'.format(name, age)
	print(message)

	if needs_stars:
		print('*******')

function_with_default_value('Dima')



 