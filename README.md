# File Search and Open Utility

This Python script provides a utility to search a specified directory and all its subdirectories for files with a specific extension and opens the most recently modified file found.

## How to Use

Run the script from the command line, passing two arguments:

1. The directory path to search.
2. The file extension to look for.

For example:

```
python.exe python_file.py 'H:\' '.py'
```

### Requirements

- Python environment (Python 3 recommended)
- pandas library

### Functionality

- The script will create a pandas DataFrame to store the paths, file names, and last modified times of found files.
- It filters files based on the given extension and sorts them by the last modified time in descending order.
- The script then attempts to open the most recent file. If the file cannot be found or another error occurs, it will print an error message.

Make sure to have the necessary permissions to access the directory and files you wish to search.

### Error Handling

The script checks for the correct number of arguments. If the required path and extension arguments are not provided, it displays an error message and instructions for proper usage before exiting.

```python
if len(sys.argv) < 3:
    print("Path and extension arguments are required!")
    print("Usage: python.exe 'python_file.py' 'H:\' '.py'")
    sys.exit()
```

### About the Code

The script includes several functions to handle the search and processing steps:

- `create_df()`: Initializes the DataFrame.
- `get_file_list(dir_to_search, file_extension)`: Searches for and adds files to the DataFrame.
- `sort_df(df)`: Sorts the DataFrame based on the last modified time.
- `open_path(path)`: Tries to open the file at the specified path.
- `get_path(df)`: Retrieves the path of the most recently modified file from the DataFrame.


* readme.md genenerated with GPT
