#!/usr/bin/python3

"""
Export data in CSV format
"""


import csv
import requests
import sys


def fetch_employee_data(base_url, emp_id):
    emp_response = requests.get(base_url + "users/{}".format(emp_id))
    emp_data = emp_response.json()
    emp_username = emp_data.get("username")

    tasks_response = requests.get(
        base_url + "todos",
        params={
            "userId": emp_id})
    tasks_data = tasks_response.json()

    return emp_id, emp_username, tasks_data


def export_to_csv(data, file_name):
    with open(file_name, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [csv_writer.writerow(
            [emp_id, emp_username, task.get("completed"), task.get("title")]
        ) for emp_id, emp_username, tasks_data in data for task in tasks_data]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script_name.py [user_id]")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    employee_id, employee_username, employee_tasks = fetch_employee_data(
                                                          base_url,
                                                          employee_id)

    employee_data = [(employee_id, employee_username, employee_tasks)]
    export_to_csv(employee_data, "{}.csv".format(employee_id))
