import argparse
from utils import load_tasks, save_tasks

def main():
    parser = argparse.ArgumentParser(
        description="📝 A simple to-do CLI app"
    )

    parser.add_argument("command", choices=["add", "list"], help="Command to run")

    parser.add_argument("-t", "--title", help="Title of the task")
    parser.add_argument("-d", "--description", help="Description of the task")
    parser.add_argument("-dd", "--due_date", help="Due date in YYYY-MM-DD format")

    args = parser.parse_args()

    if args.command == "list":
        load_tasks()
    elif args.command == "add":
        if args.title and args.description and args.due_date:
            save_tasks(args.title, args.description, args.due_date)
        else:
            print("❌ You must provide --title, --description, and --due_date to add a task.")

if __name__ == "__main__":
    main()
