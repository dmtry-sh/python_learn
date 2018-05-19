

class Parent:
	def call(self):
		print('Parent')

class Child(Parent):
	def call(self):
		print('Child')

class Example:
	def call(self):
		print('Ex')

def call_obj(obj):
	obj.call()

call_obj(Child())
call_obj(Parent())