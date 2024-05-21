#!/usr/bin/python3
"""
This module uses the JSONPlaceholder API to fetch data about all employees'
TODO list progress and exports a summary in JSON format.

Usage:
    ./3-dictionary_of_list_of_dictionaries.py
"""

import json  # For writing to JSON files
import requests  # For making HTTP requests

if __name__ == "__main__":
    # Define the URLs for the user and todos endpoints
    base_url = "https://jsonplaceholder.typicode.com/users/"
    users_url = "{}".format(base_url)

    # Send a GET request to the user endpoint and parse the response as JSON
    users_response = requests.get(users_url)
    users = users_response.json()

    all_users_tasks = {}

    for user in users:
        # Get the employee ID from the user
        employee_id = user['id']
        todos_url = "{}/{}/todos".format(base_url, employee_id)

        # Send a GET request tothetodosendpoint andparse the response as JSON
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        # Prepare data for JSON export
        tasks = []
        for task in todos:
            tasks.append({
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed']
            })

        all_users_tasks[employee_id] = tasks

    # Write data to a JSON file
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_users_tasks, jsonfile)
