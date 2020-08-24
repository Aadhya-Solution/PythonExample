import requests
import json


response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
print(todos)
with open("filtered_data_file.json", "w") as data_file:
    json.dump(response, data_file, indent=2)