from todocli import models
import argparse
from datetime import datetime


def main():
    manager = models.TaskManager()

    parser = argparse.ArgumentParser(prog="todocli", description="Task CLI Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Create new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("description", help="Task Title")
    add_parser.add_argument("due_date", help="Due date (YYYY-MM-DD)")

    update_parser = subparsers.add_parser("update", help="Update task")
    update_parser.add_argument("n", type=int, help="Task ID to update")
    update_parser.add_argument("--title", help="New title for the task")
    update_parser.add_argument("--description", help="New description for the task")
    update_parser.add_argument("--due_date", help="New due date (YYYY-MM-DD)")
    update_parser.add_argument(
        "--status", choices=["active", "completed"], help="New status for the task"
    )

    list_parser = subparsers.add_parser("list", help="Show all tasks")
    list_parser.add_argument(
        "--status", choices=["active", "completed"], help="Filter tasks by status"
    )

    delete_parser = subparsers.add_parser("delete", help="Remove task")
    delete_parser.add_argument("task_id", type=int, help="Task ID to delete")

    args = parser.parse_args()
    try:
        if args.command == "add":
            due_date = datetime.strptime(args.due_date, r"%Y-%m-%d")
            manager.create(args.title, args.description, due_date)
            print(f"Created task: {args.title}")

            manager.save()
        elif args.command == "list":
            tasks = manager.get_tasks()
            if args.status:
                tasks = [t for t in tasks if t.status.name == args.status]

            if len(tasks) == 0:
                print("There are no tasks saved")
                return

            print(f"Tasks ({len(tasks)}):")
            for i, task in enumerate(tasks):
                print(
                    f"{i + 1}. {task.title} | Due: {task.due_date.date()} | Status: {task.status.value}"
                )

        elif args.command == "update":
            task = manager.retrieve_task(args.n - 1)

            if args.title:
                task.title = args.title
            if args.description:
                task.description = args.description
            if args.due_date:
                task.due_date = datetime.strptime(args.due_date, r"%Y-%m-%d")
            if args.status:
                task.status = models.Task.Status.from_str(args.status.upper())

            print(f"Updated task: {task.title}")

            manager.save()

        elif args.command == "delete":
            deleted = manager.delete(args.task_id - 1)
            print(f"Deleted task: {deleted.title}")
            manager.save()
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
