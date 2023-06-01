import json

with open ('mydata.json', 'r') as f:
    parsed = json.loads(f.read())


print(parsed['people'][0]['name'])
