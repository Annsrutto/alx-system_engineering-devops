#!/usr/bin/python3
"""Export employee TODO tasks to stdout"""

import sys
import requests


def employee_todo_progress(employee_id):
    """Display employee's completed TODO tasks"""
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name", "Unknown")

    # Fetch user's TODO list
    todos_url = f"{base_url}/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Count completed tasks and prepare task list
    num_completed_tasks = 0
    task_list = ""
    for task in todos_data:
        if task.get("completed"):
            num_completed_tasks += 1
            task_list += f"\t{task.get('title')}\n"

    # Display progress
    print(f"Employee {employee_name} is done with tasks "
          f"({num_completed_tasks}/{len(todos_data)}):")
    print(task_list, end="")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_todo_progress(int(employee_id))
