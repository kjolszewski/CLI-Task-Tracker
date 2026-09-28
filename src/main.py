# starts program, parses command, calls appropriate functionality and displays results
import json, requests, argparse
from tabulate import tabulate 


headers = ["ID", "Task", "Priority", "Due Date", "Status"]

print(tabulate([], headers=headers, tablefmt="grid"))

def main():
    parser = argparse.ArgumentParser(description="CLI Task Tracker")
    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")

    # list
    list_praser = subparsers.add_parser("list")

    # complete
    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("id", type=int)

    # delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int) 

    # edit
    edit_parser = subparsers.add_parser("edit")
    edit_parser.add_argument("id", type=int)
    edit_parser.add_argument("--title")
    edit_parser.add_argument("--priority")

    # search
    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("query")

    # statistics
    stats_parser = subparsers.add_parser("stats")

    args = parser.parse_args()

if __name__ == "__main__":
    main()