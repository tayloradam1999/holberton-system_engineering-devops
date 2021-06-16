#!/usr/bin/python3

"""
Using what you did in the task #0,
extend your Python script to export data in the CSV format.
"""

import csv
import requests
from sys import argv


def save_to_csv(employeeId):

    username = ''
    tasks = []

    userR = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(employeeId))
    todoR = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(employeeId))

    username = userR.json().get('username')
    todoR = todoR.json()

    for task in todoR:
        taskRow = []
        taskRow.append(employeeId)
        taskRow.append(username)
        taskRow.append(task.get("completed"))
        taskRow.append(task.get("title"))

        tasks.append(taskRow)

    with open("{}.csv".format(employeeId), 'w') as csvFile:
        csvwriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(tasks)

if __name__ == "__main__":
    save_to_csv(argv[1])
