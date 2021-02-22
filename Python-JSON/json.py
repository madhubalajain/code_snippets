''' Javascript object Notation'''

import json

people_string = '''
{
  "people:[
    {
      "name" : "madhu",
      "phone" : "2783729"
      "emails" : ["madhu@gmail.com", madhu1@gmail.com"
      "has_licence" : false
    },
    {
      "name" : "test",
      "phone" : "2783729"
      "emails" : ["test@gmail.com", test@gmail.com"
      "has_licence" : true
    }
  ]
}
'''

data = json.loads(people_string)

print(type(data)). # dict

# https://docs.python.org/3/library/json.html#encoders-and-decoders

print(type(data['people'])). # list

for person in data['people']:
  print(person)
  print(person[name])
  
  
# Delete phone number from object and dump in json

for person in data['people']:
  del person['phone']
  
new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)

