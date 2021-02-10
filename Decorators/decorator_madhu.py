Decorator - Dynamically Alter the functionality of Function

A decorator is a just fuction that takes another function as argumnet, add some functionality and return  another function, all of these without altering the source code of original function that you passed in


def decorator_function(original_function):
	def wrapper_function():
		print('wrapper exceuted this before {}'.format(original_function.__name__))
		return original_function()
	return wrapper_function

def display():
	print('display function ran')

decoratored_display = decorator_function(display)

decorated_display()

we can change anything in the wrapper function without doing any change to display function

@decorator_function
def display():
	print('display function ran')

display()

// display = decorator_function(display)


---------------------

def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print('wrapper exceuted this before {}'.format(original_function.__name__))
		return original_function(*args, **kwargs)
	return wrapper_function

@decorator_function
def display():
	print('display function ran')


@decorator_function
def display_info():
	print('display function ran with arguments ({},{})'.format(name, age))

display()

display_info('john', 25)



---------------------------

Class decorators

class decorator_class(object):
	
	def __init__(self, original_function):
		self.original_function = original_function

	def __call__(self, **args, **kwargs):
		rint('call method exceuted this before {}'.format(self.original_function.__name__))
		return self.original_function(*args, **kwargs)


@decorator_class
def display_info():
	print('display function ran with arguments ({},{})'.format(name, age))

display_info('john', 25)

https://www.youtube.com/watch?v=FsAPt_9Bf3U

