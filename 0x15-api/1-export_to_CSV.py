#!/usr/bin/python3
""" Python script to export data in the CSV format."""
import json
import requests
import sys


if __name__ == '__main__':
    args_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(args_id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1])).json()

    with open("{}.json".format(args_id), "w") as user_id:
        json.dump({args_id: [{
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': users.get('username')
        } for task in todos]}, user_id)
