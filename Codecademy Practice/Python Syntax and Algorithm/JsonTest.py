import json

with open('Person.json') as f:
    data = json.load(f)

print(data)
for person in data['person']:
    del person['pets']

with open('new_person.json', 'w') as f:
    json.dump(data, f, indent=2)