#!/usr/bin/python3

"""Export data in JSON format"""


import json
import requests
import sys


def export_to_json(user_id):
    """data exported in JSON format"""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Employee not found.")
        sys.exit(1)

    user = response.json()
    username = user.get("username")

    todos_url = f"https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todos_url, params={"userId": user_id})
    if todos_response.status_code != 200:
        print("Error: Failed to fetch TODO list.")
        sys.exit(1)

    todos = todos_response.json()
    user_tasks = []
    for todo in todos:
        user_tasks.append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        })

    user_data = {str(user_id): user_tasks}

    json_file = f"{user_id}.json"
    with open(json_file, "w") as file:
        json.dump(user_data, file)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    export_to_json(user_id)
