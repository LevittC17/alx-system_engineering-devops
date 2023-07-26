#!/usr/bin/python3

"""Dictionary of lists of dictionaries"""


import json
import requests
import sys


def get_tasks_by_user(user_id):
    """Extend the script to export JSON data"""
    response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
    tasks = response.json()
    return tasks


def export_to_json(data, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python3 script_name.py [user_id_1] [user_id_2] ...")
    else:
        all_tasks = {}
        for user_id in sys.argv[1:]:
            tasks = get_tasks_by_user(user_id)
            user_info = tasks[0]['userId'], tasks[0]['title'],
            tasks[0]['completed'], tasks[0]['username']
            all_tasks[user_id] = [{"task": task["title"],
                                   "completed": task["completed"],
                                   "username": user_info[3]} for task in tasks]

        export_to_json(all_tasks, 'todo_all_employees.json')
