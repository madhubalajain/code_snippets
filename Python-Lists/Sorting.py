

li = [9, 1, 3, 2, 4, 5]

s_li = sorted(li) # created a new sorted list and the original list will not be affected

s_li = sorted(li, reverse=True)

li.sort() # Sort the original list

li.sort(reverse=True)

# sort menthod works only on list, while sorted work on all iterable

tup = (4, 2, 1, 6)

s_tup = sorted(tup) # sort method is not available for tuple

# s_tup is list, not tuple


di = {'name' : 'corey' , 'age' : 24, 'programming_lang' : 'Java'}

s_di = sorted(di)

# returns the list of sorted keys

# ['age' ,'name', 'programming_lang']

li = [-6, -5, -1, 1 , 4, 7]

#sort based on the absolute value

s_li = sorted(li, key=abs)

# [ -1, 1, 4, -5, -6, 7]

class Employee():
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary
    
  def __repr__(self):
    return '({}, {}, ${})'.formate(self.name, self.age, self.salary)
    
  e1 = Employee('madhu', 35, 50000)
  e2 = Employee('marry', 26, 89000)
  e3 = Employee('John', 76, 56000)
  
  employees = [e1, e2, e3]
  
  def e_sort(emp):
    return emap.name
  
s_employees = sorted(employees, key=e_sort)
  
s_employees = sorted(employees, key=e_sort, reverse=True)

s_employees = sorted(employees, key=lambda e: e.name)

from operator import attrgetter
s_employees = sorted(employees, key=attrgetter('age'))








