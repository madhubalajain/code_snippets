First-Class Functions:
"A Programming language is said to have first-class fucntions if it treats functions as first-class citizens."

First-Class Citizen (Programming):
"A first-class citizen (sometimes called first-class objects) in a programming language is an entity which supports all the operations generally available to other entities. These operations typically include being passed as an argumnet, returned from function and assigned to a variable."


//assigned to a variable
def square(x):
	return x * x

f= square

print(square)
print(f(5))

//passed as an argumnet
def square(x):
	return x * x

def cube(x):
	return x * x * x

def my_map(func, arg_list):
	result = []
	for i in arg_list:
		result.append(func(i))
	return result

squares = my_map(square, [1,2,3,4,5])

print(squares)


//returning function from fuction (Closures)

def logger(msg):

	def log_messages():
		print('Log:', msg)
	return log_message

log_hi = logger('Hi !')
log_hi()














