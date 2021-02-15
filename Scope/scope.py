'''
LEGB
Local, Enclosing, Global, Built-in
'''

for a in range(2):
    x = 'global {}'.format(a)


def outer():
    # x = 'outer x'
    for b in range(3):
        x = 'outer {}'.format(b)

    def inner():
        # x = 'inner x'
        for c in range(4):
            x = 'inner {}'.format(c)
        print(x)
        print(a, b, c)

    inner()
    print(x)
    print(a, b)

outer()
print(x)
print(a)



-------------------------------
x = 'global x'

def test():
    gobal x
    x = 'local x'
    print(x)
    
test()
print(x) 

# local x
# local x

# if we comment line no. 33 and run the program, then also it works , no error is thrown for line no 41


# Built-in

import builtins

print(dir(builtins))


-------------
#enclosing scope


def outer()
    x = 'outer x'
    
    def innter()
        nonlocal x
        x = 'inner x'
        print(x)
    inner()
    print(x)
    
outer()

#Output 
inner x
inner x

