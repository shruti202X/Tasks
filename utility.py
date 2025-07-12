import pandas as pd
import os

def merge_tasks(task_file_name, other_task_files):
    
    # Read the main task file
    task_df = pd.read_csv(task_file_name)
    
    # Merge with other task files
    for other_task_file in other_task_files:
        other_task_df = pd.read_csv(other_task_file)
        task_df = pd.concat([task_df, other_task_df], ignore_index=True)
        
    # Sort by 'Date Time' column
    task_df['Date Time'] = pd.to_datetime(task_df['Date Time'])
    task_df = task_df.sort_values(by='Date Time').reset_index(drop=True)
    
    # Save back to task_file_name
    task_df.to_csv(task_file_name, index=False)
    
    # Delete other_task_files
    for other_task_file in other_task_files:
        os.remove(other_task_file)