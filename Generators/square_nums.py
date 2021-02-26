
# def square_numbers(nums):
#     for i in nums:
#         yield (i*i)

# my_nums = square_numbers([1,2,3,4,5])

my_nums = (x*x for x in [1,2,3,4,5])

print list(my_nums) # [1, 4, 9, 16, 25]

# for num in my_nums:
#     print num


------------------------------------------------
#NOn - Generator code

def square_numbers(nums):
  result = []
  for i in nums:
     result.append(i*i)
  return result

my_nums = square_numbers([1,2,3,4,5])

print(my_nums)

------------------------------------------------
#Generator code


def square_numbers(nums):
  for i in nums:
     yield(i*i)
  

my_nums = square_numbers([1,2,3,4,5])

print(my_nums)
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))


--------------------------------------
# List Comprehension

my_nums = [ x*x for x in [1,2,3,4,5]] 

--------------------------------------
# Generator 

my_nums = ( x*x for x in [1,2,3,4,5])

print my_nums
for num in my_nums:
  
#No need of above for loop, wrap through list. But we loose performance benefit 
# Generator don't keep the list in memory

print list(my_nums)
     print num        
