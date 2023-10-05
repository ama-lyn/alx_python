#!/usr/bin/python3
""" 
Uses a REST API, fetching data about a given employee
(identified by their id passed to sript as argument) &
exports the data (of all tasks owned by user) in the JSON format 
"""

import json
import requests


if __name__ == "__main__":

    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch data for all employees
    employee_data = []
    for employee_id in range(1, 11):  # Assuming employee IDs range from 1 to 10
        employee_url = "{}/users/{}".format(base_url, employee_id)
        employee_response = requests.get(employee_url)
        employee_info = employee_response.json()

        if 'name' in employee_info:
            employee_name = employee_info.get('name')
        else:
            continue  # Skip this employee if 'name' is not present

        # Fetch employee's TODO list
        todo_url = "{}/users/{}/todos".format(base_url, employee_id)
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Prepare data for JSON export
        user_tasks = []
        for task in todo_data:
            task_data = {
                "username": employee_name,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            user_tasks.append(task_data)

        employee_data.append({employee_id: user_tasks})

    # Create a JSON file for all employees' tasks
    output_filename = "todo_all_employees.json"
    with open(output_filename, 'w') as json_file:
        json.dump(employee_data, json_file)

    print("Data exported to {}.".format(output_filename))
