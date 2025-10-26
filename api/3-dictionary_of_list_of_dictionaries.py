#!/usr/bin/python3
"""Export all employee TODO lists to JSON format."""
import json
import urllib.request


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users_url = f"{base_url}/users"
    with urllib.request.urlopen(users_url) as response:
        users = json.loads(response.read().decode())

    all_data = {}

    # Loop through each user to get their tasks
    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        todos_url = f"{base_url}/todos?userId={user_id}"
        with urllib.request.urlopen(todos_url) as response:
            todos = json.loads(response.read().decode())

        all_data[user_id] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos
        ]

    # Write all data to a JSON file
    filename = "todo_all_employees.json"
    with open(filename, "w", encoding="utf-8") as jsonfile:
        json.dump(all_data, jsonfile)
