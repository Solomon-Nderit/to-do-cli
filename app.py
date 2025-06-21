import argparse
from utils import save_tasks


def main():
      parser = argparse.ArgumentParser(
        description="A simple to-do cli app"
    )
      
      parser.add_argument(
        "-t", "--title", metavar="title", required=True, 
        help="The title of your task"
    )
      
      parser.add_argument(
        "-d", "--description", metavar="description", required=True, 
        help="The description of your task."
    )
      
      parser.add_argument(
        "-dd", "--due_date", metavar="YYYY-MM-DD", required=True, 
        help="The due date of your task in YYYY-MM-DD format (e.g., 2025-06-23)"
    )
      args = parser.parse_args()

      save_tasks(args.title, args.description, args.due_date)
      
if __name__=='__main__':
      main()