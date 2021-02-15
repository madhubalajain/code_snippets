
condition = 'Test'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

    # Object Identity:  is
    This check where the object reference in memory is same or not
    
    #Python don't have switch statement, rather it has as if elif else to do that
    
    # Boolean operator
    and
    or
    not
    
    
    a = [1, 2, 3]
    b = [1, 2, 3]
    
    if( a == b) # True
        print('true')
       
    if( a is b) #False
        print('False')
        
    a = [1, 2, 3]
    b = a
    
    print(a is b) #True. print(id(a) == id(b))
    print(a == b) #True
    
    # False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.
