
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)

print(student['name'])

print(student['class']) # Throws the value exception, to overcome that use get method

print(student.get('class')) # output None

#if the value no exist, then we can pass the default value

print(student.get('class','Not Found'))

#Add the entry in the Map

student['class'] = '10th' 

#Update the value

student['name'] = 'Jane'

#Update or add the value all at a time

student.update({'name':'Jane', 'age':26, 'phone':'555-555'})

#Delete from the Map

del student['name']

#if you want to delete and get the value of deleted entry

age = student.pop('age')

print(len(student))

print(student.keys())

print(student.values())

print(student.items())

for key, value in student.items():
    print(key, value)
