#!/usr/bin/python3
"""Script to export data in the CSV format"""
import requests
import sys
import csv

# Define the base URL of the API
base_url = "https://jsonplaceholder.typicode.com"

# Get the employee ID from the command line arguments
employee_id = int(sys.argv[1])

# Send a GET request to the API to get the list of todos for the employee
todos = requests.get(f"{base_url}/todos?userId={employee_id}").json()

# Get the name of the employee from the API
employee_name = requests.get(f"{base_url}/users/{employee_id}").json()['username']

# Create a new CSV file with the employee ID as the filename
filename = f"{employee_id}.csv"
with open(filename, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
    
    # Write a row for each TODO item
    for todo in todos:
        writer.writerow([employee_id, employee_name, todo['completed'], todo['title']])

print(f"TODO list for employee {employee_id} ({employee_name}) exported to {filename}")
