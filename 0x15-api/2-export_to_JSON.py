#!/usr/bin/python3

"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""

import json
import requests
from sys import argv


def export_to_json(employeeId):

    username = ''
    userDict = {}

    userR = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(employeeId))
    todoR = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(employeeId))

    username = userR.json().get('username')
    todoJ = todoR.json()

    userDict[employeeId] = []

    for task in todoJ:
        taskDict = {}
        taskDict["task"] = task.get('title')
        taskDict["username"] = username
        taskDict["completed"] = task.get('completed')

        userDict[employeeId].append(taskDict)

    with open("{}.json".format(employeeId), 'w') as jsonFile:
        json.dump(userDict, jsonFile)

if __name__ == "__main__":
    export_to_json(argv[1])
