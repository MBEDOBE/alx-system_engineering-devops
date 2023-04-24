import requests
import json

# Define the base URL of the API
base_url = "https://jsonplaceholder.typicode.com"

# Send a GET request to the API to get the list of users
users = requests.get(f"{base_url}/users").json()

# Create a new dictionary to store the TODO list data
todo_list = {}

# Loop over each user and add their TODO items to the dictionary
for user in users:
    # Get the ID and name of the user
    user_id = user['id']
    user_name = user['username']
    
    # Send a GET request to the API to get the list of todos for the user
    todos = requests.get(f"{base_url}/todos?userId={user_id}").json()
    
    # Add a new item to the dictionary for each TODO item
    for todo in todos:
        todo_item = {
            "username": user_name,
            "task": todo['title'],
            "completed": todo['completed']
        }
        if user_id not in todo_list:
            todo_list[user_id] = []
        todo_list[user_id].append(todo_item)

# Export the TODO list data to a JSON file
filename = "todo_all_employees.json"
with open(filename, mode='w') as json_file:
    json.dump(todo_list, json_file, indent=4)

print(f"TODO list for all employees exported to {filename}")
