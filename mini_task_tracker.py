"""Menu-based Task Tracker using JSON storage and UUID task IDs."""

import json
import uuid

TASKS_FILE = "tasks.json"


def load_tasks() -> list:
    """Load tasks from the JSON file; return an empty list if it is missing or invalid."""
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            tasks = json.load(file)
            if isinstance(tasks, list):
                return tasks
            print("Invalid task data. Starting with an empty task list.")
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("The tasks.json file contains invalid JSON. Starting with an empty task list.")
        return []


def save_tasks(tasks: list) -> None:
    """Save all tasks to the JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks: list) -> None:
    """Add a new pending task with a unique UUID."""
    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    task = {
        "task_id": str(uuid.uuid4()),
        "title": title,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks(tasks: list) -> None:
    """Display tasks as a numbered list with their current status."""
    if not tasks:
        print("No tasks found. Add a task first.")
        return

    print("\nYour tasks:")
    for number, task in enumerate(tasks, start=1):
        status = "Done" if task.get("done", False) else "Pending"
        print(f"{number}. {task.get('title', 'Untitled')} [{status}]")


def get_task_number(tasks: list, action: str):
    """Ask for a 1-based task number and return its 0-based index, if valid."""
    if not tasks:
        print("There are no tasks to select.")
        return None

    try:
        number = int(input(f"Enter the task number to {action}: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

    if number < 1 or number > len(tasks):
        print(f"Invalid task number. Choose a number from 1 to {len(tasks)}.")
        return None

    return number - 1


def complete_task(tasks: list) -> None:
    """Mark the selected task as completed."""
    view_tasks(tasks)
    index = get_task_number(tasks, "complete")
    if index is None:
        return

    if tasks[index].get("done", False):
        print("This task is already completed.")
        return

    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Task marked as completed.")


def delete_task(tasks: list) -> None:
    """Delete the selected task."""
    view_tasks(tasks)
    index = get_task_number(tasks, "delete")
    if index is None:
        return

    deleted_task = tasks.pop(index)
    save_tasks(tasks)
    print(f"Task '{deleted_task.get('title', 'Untitled')}' deleted successfully.")


def main() -> None:
    """Run the task tracker menu until the user chooses Exit."""
    tasks = load_tasks()

    while True:
        print("\n--- TASK TRACKER ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue

        # i am thinking to use match here but due to requirements of assignment i use if else
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            complete_task(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
