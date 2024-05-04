# writing json file

import json


person_dict = {
  "people": [
    {
      "name": "bob",
      "age": 28,
      "weight": 80
    },
    {
      "name": "sk",
      "age": 55,
      "weight": 22
    }


  ]
}

json_string = json.dumps(person_dict, indent=3)
with open('person.json', 'w') as f:
  f.write(json_string)
