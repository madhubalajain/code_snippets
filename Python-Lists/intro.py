
# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()


list = ['History', 'Math', 'Physics', 'CompSci']
print(list)

#to print the len of List

print(len(list))

#Access the list

print(list[1]) #Math

print(list[-1]) #CompSci

print(list[0:2]) #starting from 0 and not including index2

print(list[:2]) #same as above

print(list[2:]) #Strating from index2 and till last

list.append('art') # add in end

list.insert(0,'art') # add the element at index

list = ['History', 'Math', 'Physics', 'CompSci']
list_2 = ['Art', 'Edu']

list.insert(0,list_2) # it is add list 
#[['Art', 'Edu'],'History', 'Math', 'Physics', 'CompSci']

print(list[0])
#['Art', 'Edu']

list.extend(list_2)
#['History', 'Math', 'Physics', 'CompSci','Art', 'Edu']


list.remove('Math')

list.pop()

#Reverse the list

list.reverse()

list.sort()

list.sort(reverse=True) #Reverse in descending order

sorted(list) #will not sort the actual list

num = [2,3,1,4,5]
print(min(num))
print(max(num))
print(sum(num))


#To get index of element inlist

print(list.index('Math)) #1

# To find if the value existing in the list or not
                 
print('Art' in list). 

print(sum(num)) #False

for item in list:
  print(item)
                 





