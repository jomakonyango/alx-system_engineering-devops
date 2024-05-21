#!/usr/bin/python3
"""
This module uses the JSONPlaceholder API to fetch data about an employee's
TODO list progress and exports a summary in JSON format.

Usage:
    ./2-export_to_JSON.py <employee_id>
"""

import json  # For writing to JSON files
import requests  # For making HTTP requests
import sys  # For command-line arguments

if __name__ == "__main__":
    # Check if an employee ID is provided
    if len(sys.argv) < 2:
        print('Usage: {} employee_id'.format(sys.argv[0]))
        sys.exit(1)

    # Get the employee ID from the command-line arguments
    employee_id = int(sys.argv[1])
    # Define the URLs for the user and todos endpoints
    base_url = "https://jsonplaceholder.typicode.com/users/"
    user_url = "{}{}".format(base_url, employee_id)
    todos_url = "{}/{}/todos".format(base_url, employee_id)

    # Send a GET request to the user endpoint and parse the response as JSON
    response = requests.get(user_url)
    user = response.json()
    # Send a GET request to the todos endpoint and parse the response as JSON
    response = requests.get(todos_url)
    todos = response.json()

    # Prepare data for JSON export
    tasks = []
    for task in todos:
        tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": user['username']
        })

    # Write data to a JSON file
    with open('{}.json'.format(employee_id), 'w') as jsonfile:
        json.dump({employee_id: tasks}, jsonfile)
