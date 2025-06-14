import argparse
import csv
from datetime import datetime

to_choices = ["start", "rant", "pause", "complete", "list", "checkpoint"]

parser = argparse.ArgumentParser(description="Better Manage Tasks")
parser.add_argument("--task", type=str, help="Name of the task or subtask", default=None)
parser.add_argument("--to", type=str, choices=to_choices, help="Specify action you want to perform.", default=None)
args = parser.parse_args()

task = args.task
if task is None:
    task = input("Enter Task: ")

task_file_name = task + ".csv"

to = args.to
while to not in to_choices:
    print("Please enter from "+str(to_choices)+".")
    to = input("Enter what does the message want to express: ")

print("Enter message:")
message = []
while True:
    message_line = input()
    if '\x04' in message_line: # If Ctrl D in line
        message.append(message_line.split('\x04')[0])
        break
    else:
        message.append(message_line)

message_string = '\n'.join(message)

with open(task_file_name, mode="a") as f:
    writer = csv.writer(f)
    writer.writerow([to, datetime.now().strftime(f"%d %B, %Y (%I:%M %p)"), message_string])