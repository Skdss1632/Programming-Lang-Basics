import json


my_dict = {
    "people": [
        {
        "name": "bob",
        "age": 28,
        "weight": 80
        },
        {
            "name": "anna",
            "age": 34,
            "weight": 67
        },
        {   "name": "punit",
            "age": 39,
            "weight": 21
        },
        {   "name": "akshit",
            "age": 56,
            "weight": 89
         }

   ]
}



json_string = json.dumps(my_dict, indent=3) # json.dumps() function is used to convert the dictionary into a JSON-formatted string

with open ('mydata.json', 'w') as f:
    f.write(json_string)
