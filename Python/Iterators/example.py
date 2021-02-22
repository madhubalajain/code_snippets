nums =[ 1, 2, 3]

print(dir(nums))

# look for __iter__()

iterator - an object with an state which remember where it is doing iterations. it has __next__()

i_nums = nums.__iter__() # i_num = iter(nums)

print(i_nums)
print(dir(i_nums))

print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums)) # throws StopIteration exception


while True:
    try:
      item = next(nums)
      print(item)
    except StopIteration:
      break
      
#Generators are iterator 

    current = start
    while True:
        yield current
        current += 1
      
