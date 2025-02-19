# To-Do List CLI Application

A command-line to-do list application built with Python, focusing on Object-Oriented Programming (OOP) principles, encapsulation, and inheritance. Supports CRUD operations, JSON persistence, and priority-based tasks.

Main purpose of the project is to learn python fundamentals.

## Features

### **Command-Line Arguments Mode**

```bash
python main.py add "Write report" "Urgent project" 2023-10-07 --priority high
python main.py list --status pending
python main.py delete 3
```

### **CLI Interface**

- Interactive command-line interface with commands like:
  - `add`: Create a new task.
  - `list`: Display all tasks.
  - `update`: Modify a task by ID.
  - `delete`: Remove a task by ID.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/todo-list-cli.git
   cd todo-list-cli
   ```

2. **Run the application**

   ```bash
   python cli.py
   ```

## Usage examples

| Command                                                 | Result                    |
| ------------------------------------------------------- | ------------------------- |
| `add "Buy groceries" "Milk and eggs" "2023-10-05"`      | Add a new task.           |
| `add_priority "Fix bug" "Urgent fix" "2023-10-06" high` | Add a high-priority task. |
| `list`                                                  | List all tasks.           |
| `update 1 --status completed`                           | Mark task 1 as completed. |
| `delete 1`                                              | Delete task 1.            |
