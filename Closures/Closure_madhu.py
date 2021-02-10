A closure is a record storing a function[a] together with an environment.[1] The environment is a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.[b] Unlike a plain function, a closure allows the function to access those captured variables through the closure's copies of their values or references, even when the function is invoked outside their scope.


def outer_func():
	message = 'Hi'

	def inner_func():
		print(message)
	return inner_func

my_func = outer_func()

print(my_func)
print(my_func.__name__)

my_func() 

closure is an inner function that remembers and has access to variables in the local scope in which it was created  even after the  outer function has finished its execution


def outer_func(msg):
	message = msg

	def inner_func():
		print(message)
	return inner_func

hi_func = outer_func('hi')
hello_func = outer_func('hello')

hi_func()
hello_func()


https://www.youtube.com/watch?v=swU3c34d2NQ
