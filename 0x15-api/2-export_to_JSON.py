import requests
import sys
import json

# Define the base URL of the API
base_url = "https://jsonplaceholder.typicode.com"

# Get the employee ID from the command line arguments
employee_id = int(sys.argv[1])

# Send a GET request to the API to get the list of todos for the employee
todos = requests.get(f"{base_url}/todos?userId={employee_id}").json()

# Get the name of the employee from the API
employee_name = requests.get(f"{base_url}/users/{employee_id}").json()['username']

# Create a new dictionary to store the TODO list data
todo_list = {"USER_ID": []}

# Add a new item to the dictionary for each TODO item
for todo in todos:
    todo_item = {
        "task": todo['title'],
        "completed": todo['completed'],
        "username": employee_name
    }
    todo_list["USER_ID"].append(todo_item)

# Export the TODO list data to a JSON file with the employee ID as the filename
filename = f"{employee_id}.json"
with open(filename, mode='w') as json_file:
    json.dump(todo_list, json_file, indent=4)

print(f"TODO list for employee {employee_id} ({employee_name}) exported to {filename}")
