#!/usr/bin/python3

import requests
import sys


def get_employee_tasks(employeeId):
    """ Get employee to do tasks """

    name = ''
    task_list = []
    completed_counter = 0

    userRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                           .format(employeeId))
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(employeeId))

    name = userRes.json().get('name')
    tasks = todo.json()

    for task in tasks:
        if task.get('completed') is True:
            completed_counter += 1
            task_list.append(task.get('title'))
    print("task_list: {}".format(task_list))
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed_counter, len(tasks)))

    for title in task_list:
        print("\t {}".format(title))

if __name__ == "__main__":
    get_employee_tasks(sys.argv[1])
