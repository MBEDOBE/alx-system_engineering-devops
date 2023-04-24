#!/usr/bin/python3

"""
Retrieve and process the TODO list progress of a given employee ID using the provided REST API.
"""

import requests
import sys


def main():
    """
    Retrieve and process the TODO list progress of a given employee ID.
    """
    employee_id = sys.argv[1]

    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

    if response.status_code != 200:
        print("Error: Failed to retrieve TODO list.")
        sys.exit(1)

    todos = response.json()

    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo.get("completed"))

    print(f"Employee {todos[0].get('name')} is done with {done_tasks}/{total_tasks} tasks:")

    for todo in todos:
        if todo.get("completed"):
            print(f"\t{todo.get('title')}")


if __name__ == "__main__":
    main()
