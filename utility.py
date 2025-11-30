import pandas as pd
import os
import csv

def merge_tasks(task_file_name, other_task_files):
    
    # Read the main task file
    if task_file_name.endswith(".xlsx"):
        task_df = pd.read_excel(task_file_name)
        for other_task_file in other_task_files:
            other_task_df = pd.read_excel(other_task_file)
            task_df = pd.concat([task_df, other_task_df], ignore_index=True)
    else:
        task_df = pd.read_csv(task_file_name)
        for other_task_file in other_task_files:
            other_task_df = pd.read_csv(other_task_file)
            task_df = pd.concat([task_df, other_task_df], ignore_index=True)
        
    # Sort by 'Date Time' column
    task_df['Date Time Standard'] = pd.to_datetime(task_df['Date Time'], format='%d %B, %Y (%I:%M %p)')
    # Date Time Standard is like YYYY-MM-DD HH:MM:SS

    # Sort based on Date Time Data Type Column
    task_df = task_df.sort_values(by='Date Time Standard').reset_index(drop=True)

    # Remove Date Time Standard Column
    task_df = task_df.drop(columns=['Date Time Standard'])
    
    # Save back to task_file_name
    if task_file_name.endswith(".xlsx"):
        with pd.ExcelWriter(task_file_name) as writer:
            task_df.to_excel(writer, sheet_name="Log", index=False)
    else:
        task_df.to_csv(task_file_name, index=False)
    
    # Delete other_task_files
    for other_task_file in other_task_files:
        os.remove(other_task_file)
