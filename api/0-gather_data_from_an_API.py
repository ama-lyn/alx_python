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
print("Employee {} is done with tasks ({}/{}):".format(employee_name,
      completed_tasks, total_tasks))

# Display completed task titles
for task in todo_data:
    if task.get("completed"):
        formatted_task_title = "\t{} ".format(task.get("title"))
        print(formatted_task_title)
