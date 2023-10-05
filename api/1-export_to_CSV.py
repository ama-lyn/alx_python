""" Uses a REST API, fetching data about a given employee
    (identified by their id passed to sript as argument) &
    exports the data (of all tasks owned by user) in the CSV format
"""

import csv
import requests
import sys


base_url = "https://jsonplaceholder.typicode.com"
employee_id = sys.argv[1]

# Fetch employee details
employee_url = "{}/users/{}".format(base_url, employee_id)
employee_response = requests.get(employee_url)
employee_data = employee_response.json()

if 'name' not in employee_data:
    print("Employee not found.")
    sys.exit(1)

employee_name = employee_data.get('name')

# Fetch employee's TODO list
todo_url = "{}/users/{}/todos".format(base_url, employee_id)
todo_response = requests.get(todo_url)
todo_data = todo_response.json()

# Calculate progress
total_tasks = len(todo_data)
completed_tasks = sum(1 for task in todo_data if task.get("completed"))

# Display progress
print("Employee {} is done with tasks({}/{}):".format(employee_name,
      completed_tasks, total_tasks))

# Display completed task titles
for task in todo_data:
    if task.get("completed"):
        formatted_task_title = "\t {}".format(task.get("title"))
        print(formatted_task_title)


# Export data in CSV
file_name = '{}.csv'.format(employee_id)
with open(file_name, mode='w', newline='',) as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)

    # header
    csv_writer.writerow(
        ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

    # write each csv row
    for task in todo_data:
        csv_writer.writerow([employee_id, employee_name,
                            task['completed'], task['title']])
