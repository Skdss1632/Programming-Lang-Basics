import json

with open ('mydata.json', 'r') as f:
    parsed = json.loads(f.read())
    for key, value in parsed.items():
        print(key)



