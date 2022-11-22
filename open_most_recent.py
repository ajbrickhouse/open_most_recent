import os
import pandas as pd
import time
import sys

# Search a dir and it's subdir for file with a specific extension, and opens the most recent found.

# get first and second arguments from command line 
try:
    Directory_to_Search = str(sys.argv[1])
    Filetype_to_Open = str(sys.argv[2])
except:
    if len(sys.argv) < 2:
        print("Path and exention arguments are required!")
        print("python.exe 'python_file.py' 'H:\' '.py'")
    sys.exit()

# create a dataframe with columns: path, file name, last modified time (datetime)
def create_df():
    df = pd.DataFrame(columns=['path', 'file_name', 'formated_time', 'last_modified_time'])
    return df

# get list of all files in a directory and sub directorys, add result to df
def get_file_list(dir_to_search, file_extension):
    df = create_df()
    for root, dirs, files in os.walk(dir_to_search):
        for file in files:
            path_ = f'{root}\{file}'
            time_ = os.path.getctime(path_)

            if file.endswith(file_extension):
                df = pd.concat([df, pd.DataFrame.from_records([{ 'path': os.path.join(root, file), 'file_name': file, 'formated_time': time.ctime(time_), 'last_modified_time': time_ }])])
                print(file)
    return df

# filter df by file name extension and sort by last modified time in descending order
def sort_df(df):
    df = df.sort_values(by='last_modified_time', ascending=False)
    return df

# try path and open if it exists
# if not, print error message
def open_path(path):
    try:
        os.startfile(path)
    except FileNotFoundError:
        print(f'File not found: {path}')
    except:
        print(f'{path} failed to open.')

# get path from first row of df
def get_path(df):
    path = df.iloc[0]['path']
    return path

df = create_df()

print("Created DF...")

df = get_file_list(Directory_to_Search, Filetype_to_Open)

print("File list parsed...")

df = sort_df(df)

print("DF Filtered...")

print(df)

path_mr = get_path(df)

open_path(path_mr)
