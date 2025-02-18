# To-Do List CLI Application

A command-line to-do list application built with Python, focusing on Object-Oriented Programming (OOP) principles, encapsulation, and inheritance. Supports CRUD operations, JSON persistence, and priority-based tasks.

Main purpose of the project is to learn python fundamentals.

## Features

### Interaction Modes

### 1. **REPL Mode (Default)**

Run the application without arguments to enter an interactive shell:

```bash
python main.py
```

```shell
> add "Buy groceries" "Milk and eggs" 2023-10-05
> Task created with ID 1
> list

1. [Pending] Buy groceries (Due: 2023-10-05)
> exit
```

### 2. **Command-Line Arguments Mode**

```bash
python main.py add "Write report" "Urgent project" 2023-10-07 --priority high
python main.py list --status pending
python main.py delete 3
```

## Core

### 1. **Task Management**

- **`Task` Class**
  - Attributes: `title`, `description`, `due_date`, `status` (e.g., "Pending", "Completed").
  - Magic Methods: `__str__` (human-readable format), `__repr__` (developer-friendly string).
- **`PriorityTask` Class** (Inherits from `Task`)
  - Adds a `priority` attribute (e.g., "Low", "Medium", "High").
  - Overrides `__str__` to include priority information.

### 2. **Task Manager**

- **`TaskManager` Class**
  - Handles CRUD operations:
    - **Create**: Add new tasks (including priority tasks).
    - **Read**: List all tasks, filter by status/priority, or view a specific task by ID.
    - **Update**: Modify task attributes (e.g., mark as completed, change due date).
    - **Delete**: Remove tasks by ID.
  - Persistence:
    - Save tasks to a JSON file (`tasks.json`).
    - Load tasks from JSON on startup.
  - Uses instance methods for core logic and class methods for file operations.

### 3. **User Management**

- **`User` Class**
  - Attributes: `username`, `user_id`, and associated `TaskManager` instance.
  - Encapsulates task management logic for a specific user.

### 4. **JSON Storage**

- Tasks are automatically saved to `tasks.json` after modifications.
- Data is loaded from `tasks.json` when the application starts.

### 5. **CLI Interface**

- Interactive command-line interface with commands like:
  - `add`: Create a new task.
  - `list`: Display all tasks.
  - `update`: Modify a task by ID.
  - `delete`: Remove a task by ID.
  - `save`/`load`: Manually trigger JSON persistence.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/todo-list-cli.git
   cd todo-list-cli
   ```

2. **Run the application**
   ```bash
   python main.py
   ```

## Usage examples

| Command                                                 | Result                    |
| ------------------------------------------------------- | ------------------------- |
| `add "Buy groceries" "Milk and eggs" "2023-10-05"`      | Add a new task.           |
| `add_priority "Fix bug" "Urgent fix" "2023-10-06" high` | Add a high-priority task. |
| `list`                                                  | List all tasks.           |
| `update 1 --status completed`                           | Mark task 1 as completed. |
| `delete 1`                                              | Delete task 1.            |
| `save`                                                  | Force-save tasks to JSON. |
| `exit`                                                  | Exit the application.     |
