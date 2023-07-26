#!/usr/bin/python3

"""Export data in JSON format"""


import json
import requests
import sys


def fetch_user_info(url, user_id):
    user_response = requests.get(url + "users/{}".format(user_id))
    user_data = user_response.json()
    username = user_data.get("username")

    tasks_response = requests.get(url + "todos", params={"userId": user_id})
    tasks_data = tasks_response.json()

    return user_id, username, tasks_data


def export_to_json(data, file_name):
    with open(file_name, "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script_name.py [user_id]")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user_id, username, tasks_data = fetch_user_info(base_url, user_id)

    user_tasks = []
    for task in tasks_data:
        task_title = task.get("title")
        task_completed = task.get("completed")
        user_tasks.append({"task": task_title, "completed":
                           task_completed, "username": username})

    todo_data = {user_id: user_tasks}
    export_to_json(todo_data, "{}.json".format(user_id))
