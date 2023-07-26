#!/usr/bin/python3

"""
Return information of a given employee given
their ID using REST API
"""


import requests
import sys


def get_employee_data(api_url, employee_id):
    """Pass API URL, get employee id"""
    employee_response = requests.get(api_url + "users/{}".format(employee_id))
    employee_data = employee_response.json()
    tasks_response = requests.get(
        api_url + "todos",
        params={
            "userId": employee_id})
    tasks_data = tasks_response.json()
    return employee_data, tasks_data


def print_completed_tasks(employee_name, completed_tasks, total_tasks):
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))
    [print("\t {}".format(task)) for task in completed_tasks]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script_name.py [user_id]")
        sys.exit(1)

    base_api_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    employee_data, tasks_data = get_employee_data(base_api_url, employee_id)

    completed_tasks = [task.get("title")
                       for task in tasks_data if task.get("completed")]
    employee_name = employee_data.get("name")

    print_completed_tasks(employee_name, completed_tasks, len(tasks_data))
