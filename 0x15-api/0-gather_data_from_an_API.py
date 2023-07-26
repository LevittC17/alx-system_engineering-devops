#!/usr/bin/python3

"""
Given employee ID, returns information about his/her
TODO list progress
"""


import requests
import sys


def employee_todo_list(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data['name']
        total_tasks = len(todos_data)
        done_tasks = sum(1 for task in todos_data if task['completed']

        print(f'Employee {employee_name} is done with tasks({done_tasks} /
                         {total_tasks}): ')
        for task in todos_data:
            if task['completed']:
            print(f'\t{task["title"]}')

    except requests.exceptions.RequestException as e:
        print('Error occurred while fethcing data from the API:', e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 gather_data_from_an_API.py <employee_id>')
    else:
        employee_id=int(sys.argv[1])
        employee_todo_list(employee_id)
