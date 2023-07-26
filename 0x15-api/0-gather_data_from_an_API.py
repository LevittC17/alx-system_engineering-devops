#!/usr/bin/python3

"""
Return information of a given employee given
their ID using REST API
"""


import requests
import sys


def get_employee_todo_list(employee_id):
    """Get REST API URLsm employee ID and task url """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch user data
        response_user = requests.get(user_url)
        response_user.raise_for_status()
        user_data = response_user.json()
        employee_name = user_data["name"]

        # Fetch todo list data
        response_todo = requests.get(todo_url)
        response_todo.raise_for_status()
        todo_data = response_todo.json()

        # Calculate the number of done tasks
        done_tasks = [task for task in todo_data if task["completed"]]
        number_of_done_tasks = len(done_tasks)
        total_number_of_tasks = len(todo_data)

        # Display the results
        print(
            f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
        for task in done_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyError:
        print(f"Error: Invalid employee ID ({employee_id}).")
        sys.exit(1)
    except ValueError:
        print(f"Error: Invalid JSON response from the API.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list(employee_id)
