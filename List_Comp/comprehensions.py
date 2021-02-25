nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
  my_list.append(n)
print my_list

#list comprehession

my_list [ n for n in nums]

print [n for n in nums]

# I want 'n*n' for each 'n' in nums
# my_list = []
# for n in nums:
#   my_list.append(n*n)
# print my_list

my_list = [ n*n for n in nums]

# Using a map + lambda
# my_list = map(lambda n: n*n, nums)
# print my_list

# the above code can be replaced as with Line no 21

# I want 'n' for each 'n' in nums if 'n' is even
# my_list = []
# for n in nums:
#   if n%2 == 0:
#     my_list.append(n)
# print my_list

my_list = [ n for n in nums if n%2 == 0]

# Using a filter + lambda
# my_list = filter(lambda n: n%2 == 0, nums)
# print my_list

# the above code can be replaced as with Line no 36

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# my_list = []
# for letter in 'abcd':
#   for num in range(4):
#     my_list.append((letter,num))
# print my_list

my_list [(letter, num) for letter in 'abcd' for num in range(4)]

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print zip(names, heros)

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print my_dict

my_dict = {name : hero for name , hero in zip(names,heros)}

# If name not equal to Peter

my_dict = {name : hero for name , hero in zip(names,heros) if name != 'Peter'}

# Set Comprehensions
# nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print my_set

my_set = { n*n for n in nums}

# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)

my_gen = (n*n for n in nums) 

# for i in my_gen:
#     print i
