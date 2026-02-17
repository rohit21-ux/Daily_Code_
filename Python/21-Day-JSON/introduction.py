# JSON is used in :
#                  1. APIs 
#                  2. Web development
#                  3. backend systems
#                  4. Storing structured data
#                  5. Node.js - python communication
#                  6. Configuration files

# JSON stands for javascript object notation.

# it looks like python dictionary
{
    "name" : "Rohit",
    "age" : 21,
    "Skills" : ["Python", "DSA"]
}

import json

data = {
    "name" : "Rohit",
    "age" : 21,
    "Skills" : ["Python", "DSA"]
}

# converting python dictionary to json string
json_data = json.dumps(data)  # dumps() is used to convert python dictionary to json string

print(json_data)

# converting json string to python dictionary
import json

json_string = '{"name " :"Rohit","age":21}'

python_data = json.loads(json_string) # loads() is used to convert json string to python dictionary
print(python_data)

# file handling with json
import json

data = {
    "username": "rohit123",
    "password": "securepass"
}

with open("user.json", "w") as file:
    json.dump(data, file)