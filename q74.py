import json

with open("filename.json", "r") as file:
    data = json.load(file)
    print(data)
