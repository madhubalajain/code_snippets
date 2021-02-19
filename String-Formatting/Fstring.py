first_name = 'madhu
last_name = 'jain'

sentence = 'My name is {} {}'.format(first_name, last_name)

sentence = f'My name is {first_name} {last_name}'

sentence = f'My name is {first_name.upper()} {last_name.upper()}'

person = {'name' : 'madhu, "age': 23}

sentence = 'My name is {} and age is'.format(person['name'], person['age'])

sentence = f"My name is {person['name']} and age is {person['age']}"

# mind the " quotes

calculation = f'4 times 11 is {4*11}'

for n in range(1, 11)
  sentence = f'The value of n is {n:02}'
  print(sentence)
  
  
pi = 3.1415
sentence = f'pi is equal to {pi:.4f}'
print(sentence)
  
from datetime import datetime

birthday = datetime(1900, 1, 1)

sentece = f'Jenn has birthday on {birtday:%B %d %Y}'
  
