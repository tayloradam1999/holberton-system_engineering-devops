#!/usr/bin/python3

"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""

import json
import requests


def dict_of_lists_of_dicts():

    usersAndTasks = {}

    userJ = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todoJ = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    userInfo = {}
    for user in userJ:
        userInfo[user['id']] = user['username']

    for task in todoJ:
        if usersAndTasks.get(task['userId'], False) is False:
            usersAndTasks[task['userId']] = []
        task_dict = {}
        task_dict['username'] = userInfo[task['userId']]
        task_dict['task'] = task['title']
        task_dict['completed'] = task['completed']

        usersAndTasks[task['userId']].append(task_dict)

    with open("todo_all_employees.json", 'w') as jsonFile:
        json.dump(usersAndTasks, jsonFile)

if __name__ == "__main__":
    dict_of_lists_of_dicts()
