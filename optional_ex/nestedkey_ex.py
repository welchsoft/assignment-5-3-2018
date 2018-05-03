ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

#print ramit email
print(ramit['email'])

#place intersts into array and call the first entry
interests = ramit['interests']

print(interests[0])

#fill array with ramit friends
friends = ramit['friends']

#jasmine is the first entry of friends array
jasmine = friends[0]

print(jasmine['email'])

#jan is the second entry of friends array
jan = friends[1]

jan_interest = jan['interests']
# print jan interests
print(jan_interest[1])
