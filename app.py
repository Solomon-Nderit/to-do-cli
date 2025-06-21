import argparse
from utils import load_tasks, save_tasks, complete, delete, list_todays_tasks

def main():
    parser = argparse.ArgumentParser(
        description="📝 A simple to-do CLI app"
    )

    parser.add_argument("command", choices=["add", "list","complete","delete"], help="Command to run")

    parser.add_argument("-t", "--title", help="Title of the task")
    parser.add_argument("-d", "--description", help="Description of the task")
    parser.add_argument("-dd", "--due_date", help="Due date in YYYY-MM-DD format")
    parser.add_argument("-c", "--complete", help="Mark tasks as complete by id.")
    parser.add_argument("-del", "--delete", help="Delete tasks by ID")
    parser.add_argument("-td", "--today", action="store_true", help = "List tasks due today")


    args = parser.parse_args()

    try:
        if args.command == "list":
            if args.today:
                list_todays_tasks()
            else:
                load_tasks()
        elif args.command == "add":
            if args.title and args.description and args.due_date:
                save_tasks(args.title, args.description, args.due_date)
            else:
                print("❌ You must provide --title, --description, and --due_date to add a task.")
        elif args.command == 'complete':
            if args.complete:
                complete(args.complete)
        elif args.command == 'delete':
            delete(args.delete)
    except Exception as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()
