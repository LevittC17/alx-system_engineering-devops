#!/usr/bin/python3

"""
Export data in CSV format
"""


import csv
import requests
import sys


def export_to_csv(user_id):
    """ code base = task 1:: export to csv"""
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

    csv_file = f"{user_id}.csv"
    with open(csv_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([user_id, username, str(
                todo.get("completed")), todo.get("title")])


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    export_to_csv(user_id)
