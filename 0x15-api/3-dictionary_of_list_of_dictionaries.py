#!/usr/bin/python3

"""Dictionary of lists of dictionaries"""


import json
import requests


def fetch_users(url):
    response = requests.get(url + "users")
    users = response.json()
    return users

def fetch_tasks_by_user(url, user_id):
    response = requests.get(url + "todos", params={"userId": user_id})
    tasks = response.json()
    return tasks

def export_to_json(data, file_name):
    with open(file_name, "w") as json_file:
        json.dump(data, json_file)

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    all_users = fetch_users(base_url)
    todo_data = {}

    for user in all_users:
        user_id = user["id"]
        user_name = user["username"]
        tasks = fetch_tasks_by_user(base_url, user_id)
        user_tasks = []

        for task in tasks:
            task_title = task["title"]
            task_completed = task["completed"]
            user_tasks.append({"task": task_title, "completed": task_completed, "username": user_name})

        todo_data[user_id] = user_tasks

    export_to_json(todo_data, "todo_all_employees.json")
