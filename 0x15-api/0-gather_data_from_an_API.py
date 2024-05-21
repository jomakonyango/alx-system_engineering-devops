#!/usr/bin/python3
"""
This module uses the JSONPlaceholder API to fetch data about an employee's
TODO list progress and prints a summary in the console.

Usage:
    ./0-gather_data_from_an_API.py <employee_id>
"""

import requests  # For making HTTP requests
import sys  # For command-line arguments

if __name__ == "__main__":
    # Check if an employee ID is provided
    if len(sys.argv) < 2:
        print('Usage: {} employee_id'.format(sys.argv[0]))
        sys.exit(1)

    # Get the employee ID from the command-line arguments
    employee_id = sys.argv[1]
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

    # Filter the todos to get the ones that are completed
    done_tasks = [task for task in todos if task.get('completed') is True]
    # Get the total number of tasks
    total_tasks = len(todos)

    # Print the employee's progress
    print("Employee {} is done with tasks({}/{}):".format(
        user['name'], len(done_tasks), total_tasks))
    # Print the titles of the completed tasks
    for task in done_tasks:
        print("\t {}".format(task['title']))
