import argparse
import csv
from datetime import datetime
import os
from utility import *

to_choices = ["start", "rant", "pause", "complete", "list", "checkpoint", "merge"]

parser = argparse.ArgumentParser(description="Better Manage Tasks")
parser.add_argument("--task", type=str, help="Name of the task or subtask", default=None)
parser.add_argument("--to", type=str, choices=to_choices, help="Specify action you want to perform.", default=None)
args = parser.parse_args()

task = args.task
if task is None:
    task = input("Enter Task: ")

task_file_name = task + ".csv"

to = args.to
if to not in to_choices:
    to = input("Enter message tag: ")

while to not in to_choices:
    print("------------------------------------------------------------------")
    print("Message Tag: What does your message want to express?")
    print("- 'list': To describe or list down the task.")
    print("- 'start': Starting of the task, after a break.")
    print("- 'rant': Rant about the task.")
    print("- 'checkpoint': Completion of a sub task.")
    print("- 'pause': A short or long pause in the task.")
    print("- 'complete': Completion of the task.")
    print("- 'merge': To merge it with other tasks.")
    print("------------------------------------------------------------------")
    to = input("Enter message tag: ")

if to == 'merge':
    other_tasks = {}
    other_task = input("Enter other task: ")
    while other_task!="":
        if os.path.exists(other_task+".csv") == False:
           print("No such file exists. For archive tasks, enter like archive/{task_name}.")
        else:
            other_tasks.add(other_task+".csv")
        other_task = input("Enter another task to add, else simply press enter: ")
    merge_tasks(task_file_name, other_tasks)

print("Enter message (use Ctrl+D to end):")
message = []
while True:
    message_line = input()
    if '\x04' in message_line: # If Ctrl D in line
        message.append(message_line.split('\x04')[0])
        break
    else:
        message.append(message_line)

message_string = '\n'.join(message)

heading = []
if os.path.exists(task_file_name) == False:
    heading = ["Tag", "Original Task", "Date Time", "Message"]

with open(task_file_name, mode="a") as f:
    writer = csv.writer(f)
    if len(heading)>0:
        writer.writerow(heading)
    writer.writerow([to, task, datetime.now().strftime(f"%d %B, %Y (%I:%M %p)"), message_string])