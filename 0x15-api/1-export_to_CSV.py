#!/usr/bin/python3

"""
Export data in CSV format
"""


import sys
import requests
import csv


def todo_list_progress(employee_id):
    """code base = task 1"""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_response.raise_for_status()
        todos_response.raise_for_status()

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_id = user_data["id"]
        employee_name = user_data["username"]

        csv_file = f"{employee_id}.csv"
        with open(csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for todo in todos_data:
                writer.writerow([employee_id, employee_name,
                                 str(todo["completed"]), todo["title"]])
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyError:
        print("Error: Employee not found.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Please provide a valid employee ID as a parameter.")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todo_list_progress(employee_id)
