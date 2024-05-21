#!/usr/bin/python3
"""
This module uses the JSONPlaceholder API to fetch data about an employee's
TODO list progress and exports a summary in CSV format.

Usage:
    ./1-export_to_CSV.py <employee_id>
"""

import csv  # For writing to CSV files
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

    # Open a CSV file for writing
    with open('{}.csv'.format(employee_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        # Write each task to the CSV file
        for task in todos:
            writer.writerow([employee_id, user['name'],
                             task['completed'], task['title']])
