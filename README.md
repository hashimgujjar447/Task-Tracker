# Mini Task Tracker

A simple command-line task tracker built with Python. It allows users to add, view, complete, and delete tasks. Tasks are stored in a JSON file so they can be loaded again when the program is restarted.

## Features

- Add tasks with a title.
- View all tasks in a numbered list.
- See each task's status: `Pending` or `Done`.
- Mark a task as completed.
- Delete a task.
- Assign each task a unique UUID.
- Save tasks to `tasks.json` and load them at startup.
- Handle empty titles, invalid menu choices, and invalid task numbers.

## Requirements

- Python 3.10 or later
- No third-party packages required.

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project directory.
3. Run:

   ```bash
   python mini_task_tracker.py
   ```

4. Follow the menu displayed in the terminal.

## Menu Options

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit

## Data Storage

Tasks are stored in `tasks.json` in the same directory as the program. The file is created automatically when tasks are saved. Each task contains:

- `id`: unique task identifier (UUID)
- `title`: task title
- `done`: completion status (`false` for Pending, `true` for Done)

Example:

```json
[
  {
    "id": "a-unique-uuid",
    "title": "Read a book",
    "done": false
  }
]
```

## Project Structure

```text
mini-task-tracker/
├── mini_task_tracker.py
├── README.md
└── tasks.json   # Created automatically when the program saves tasks
```

## Concepts Practised

- Python functions
- Lists and dictionaries
- Loops and conditional statements
- `match`/menu-driven program flow (if used in the implementation)
- JSON file handling with `json.load()` and `json.dump()`
- Exception handling
- UUID generation

## Author

Muhammad Hashim
Created as a Python Week 1 / Day 2 mini project.
