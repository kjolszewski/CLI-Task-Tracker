# starts program, parses command, calls appropriate functionality and displays results
import json, requests, argparse
from display import show_tasks

def add(args):
    print(f"Adding task...") 

def list_tasks(args):
    print(f"Listing tasks...")

def complete_task(args):
    print(f"Completed tasks...")

def delete_task(args):
    print(f"Deleting tasks...")

def edit_task(args):
    print(f"Editting task...")

def search_task(args):
    print(f"Searching tasks...")

def display_tasks(args):
    print(f"Displaying tasks...")

def main():
    parser = argparse.ArgumentParser(description="CLI Task Tracker")
    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add)

    # list
    list_parser = subparsers.add_parser("list")
    list_parser.set_defaults(func=list_tasks)

    # complete
    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("id", help="mark a task as complete through its ID", type=int)
    complete_parser.set_defaults(func=complete_task)

    # delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", help="delete a task through its ID", type=int) 
    delete_parser.set_defaults(func=delete_task)

    # edit
    edit_parser = subparsers.add_parser("edit")
    edit_parser.add_argument("id", help="find task to edit through its ID", type=int)
    edit_parser.add_argument("--title")
    edit_parser.add_argument("--priority")
    edit_parser.set_defaults(func=edit_task)


    # search
    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("query")
    search_parser.set_defaults(func=search_task)

    # statistics
    stats_parser = subparsers.add_parser("stats")
    stats_parser.set_defaults(func=display_stats)

    args = parser.parse_args()
    args.func(args)

show_tasks(tasks)

if __name__ == "__main__":
    main()