#!/usr/bin/python3
"""A Python script that uses REST API for a given employee ID,
returns information about his/her TODO list progress"""
import requests
import sys


def get_employee_todo_tasks(id):
    """Retrieves and displays TODO list progress for a given employee ID."""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    response = requests.get(url)
    response_json = response.json()
    employee_name = response_json.get("name")

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(url)
    todos_json = todos.json()
    total_tasks = len(todos_json)

    num_completed_tasks = 0
    task_list = ""

    for task in todos_json:
        if task.get("completed") is True:
            num_completed_tasks += 1
            task_list += "\t " + task.get("title") + "\n"

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          num_completed_tasks,
                                                          total_tasks))
    print(task_list[:-1])


if __name__ == "__main__":
    get_employee_todo_tasks(sys.argv[1])
