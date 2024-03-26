#!/usr/bin/python3

import requests
import sys


def get_employee_todo_progress(employee_id):
    """Retrieves and displays TODO list progress for a given employee ID."""
    # Validate employee ID (positive integer)
    if not isinstance(employee_id, int) or employee_id <= 0:
        raise ValueError("Employee ID must be a positive integer.")

    # Build API endpoint URL
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Send GET request using requests library
    response = requests.get(url)

    # Check for successful response
    if response.status_code == 200:
        todos = response.json()

    # Count completed tasks
    completed_tasks = sum(todo.get("completed", False) for todo in todos)
    total_tasks = len(todos)

    # Display progress information
    print(f"Employee {todos[0].get('title', 'Unknown')} is done with tasks"
          f"({completed_tasks}/{total_tasks}):")

    # Display completed task titles
    for todo in todos:
        if todo.get("completed", False):
            print(f"\t{todo.get('title', 'Unknown')}")
        else:
            print(f"Error retrieving data: {response.status_code}")


if __name__ == "__main__":
    # Get employee ID input from user (assuming integer input)
    employee_id = int(input("Enter employee ID: "))

    # Retrieve and display progress
    get_employee_todo_progress(employee_id)
