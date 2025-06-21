import argparse
from utils import load_tasks, save_tasks, complete

def main():
    parser = argparse.ArgumentParser(
        description="📝 A simple to-do CLI app"
    )

    parser.add_argument("command", choices=["add", "list","complete"], help="Command to run")

    parser.add_argument("-t", "--title", help="Title of the task")
    parser.add_argument("-d", "--description", help="Description of the task")
    parser.add_argument("-dd", "--due_date", help="Due date in YYYY-MM-DD format")
    parser.add_argument("-c", "--complete", help="Mark tasks as complete by id.")

    

    args = parser.parse_args()

    if args.command == "list":
        load_tasks()
    elif args.command == "add":
        if args.title and args.description and args.due_date:
            save_tasks(args.title, args.description, args.due_date)
        else:
            print("❌ You must provide --title, --description, and --due_date to add a task.")
    elif args.command == 'complete':
        if args.complete:
            complete(args.complete)


if __name__ == "__main__":
    main()
