#!/usr/bin/python3
"""Export employee TODO list data to JSON format."""
import json
import sys
import urllib.request


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: ./2-export_to_JSON.py <employee_id>")

    emp_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    user_url = f"{base_url}/users/{emp_id}"
    with urllib.request.urlopen(user_url) as response:
        user = json.loads(response.read().decode())

    # Fetch employee tasks
    todos_url = f"{base_url}/todos?userId={emp_id}"
    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode())

    username = user.get("username")
    data = {
        emp_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }

    filename = f"{emp_id}.json"
    with open(filename, "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile)
