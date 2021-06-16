#!/usr/bin/python3

import requests
import sys

def get_employee_tasks(employeeId):

    name = ''
    task_list = []
    completed_counter = 0

    userRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employeeId))
    todoRes = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employeeId))

    name = userRes.json().get('name')
    print("Name: {}".format(name))
    
    todoJson = todoRes.json()

    for task in todoJson:
        if task.get('completed') is True:
            completed_counter += 1
            task_list.append(task.get('title'))
    print("task_list: {}".format(task_list))
    print("Employee {} is done with tasks({}/{}):".format(name, completed_counter, len(todoJson)))

    for title in task_list:
        print("\t {}".format(title))

    return 0


if __name__ == "__main__":
    get_employee_tasks(sys.argv[1])