#!/usr/bin/python3

"""
Return information of a given employee given
their ID using REST API
"""


import requests
import sys


def get_employee_todo_list_progress(employee_id):
    """Pass API URL, get employee id"""
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

        empName = user_data["name"]
        totTasks = len(todos_data)
        doneTasks = sum(1 for todo in todos_data if todo["completed"])

        print(f"Employee {empName} done with tasks({doneTasks}/{totTasks}):")
        for todo in todos_data:
            if todo["completed"]:
                print(f"\t{todo['title']}")
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
    get_employee_todo_list_progress(employee_id)
