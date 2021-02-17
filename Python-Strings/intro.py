
greeting = 'Hello'
name = 'Michael'

print(help(str.lower))

# if the string variable contains ', then enclose them in "" and vica versa

# if the string is multi-line then enclose them in 3 """ """

message = "Bobby's world"

message = 'Bobby"s world"

message = 'Bobby\'s world'

message = """Bobby's world is 
on next line"""

message = 'Hello world'

len(message)

#access the character

message[0]

message[0:5]

# Hello - the first index is inclusive(0) and 2nd is not(5)

message[:5] #Hello

message[6:11] #world

message[6:] #world

message.lower()

message.upper()

message.count('Hello') #1

message.count('l') #3

#find index

message.find('world') # 6

message.find('universe') # -1

new_message = message.replace('world', 'universe') # not making the replace in place

#if want to change in the same message variable

message = message.replace('world', 'universe') 

#Concanate 2 string

message = msg1 + msg2

greeting = ''
name = ''

message = greeting + ', '  + name + '. Welcome'

message = '{}, {} . Welcome'.format(greeting, name)

#Python F strings - on Python 3.6 n higher

message = f'{greeting}, {name} . Welcome'

#Can use functions
message = f'{greeting}, {name.upper()} . Welcome'

#if we want to find all the attributes and method that variables has access to

print(dir(name))

print(help(str))

print(help(str.lower))


