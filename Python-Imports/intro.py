import my_module

courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'Math')
print(index)


--------------------------
import my_module as mm

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
print(index)


--------------------------
from my_module import find_index , test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

--------------------------
from my_module import * 
#import everything


---------------------------------

# Python import modles from sys.path

import sys

print(sys.path)

# the first path is the current working directory

----------------------------------------------------

# if we move the modle to different diirectory, then how to import them

1. add to sys.path

import sys

sys.path.append('/dir/dir')

2. to add to PYTHONPATH

open terminal

nano ~./bash_profile

export PYTHONPATH="/dir/dir"

check in sys.path that the dir is appended









