#!/usr/bin/python3
"""script using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
    sys.exit(1)

employee_id = sys.argv[1]

# Fetch employee information
employee_resp = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
employee_resp.raise_for_status()
employee = employee_resp.json()
employee_name = employee["name"]

# Fetch employee TODO list
todo_resp = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id))
todo_resp.raise_for_status()
todos = todo_resp.json()

# Compute progress
num_done = sum(1 for todo in todos if todo["completed"])
total = len(todos)

# Display progress
print("Employee {} is done with tasks({}/{}):".format(employee_name, num_done, total))
for todo in todos:
    if todo["completed"]:
        print("\t {} {}".format("\t", todo["title"]))
