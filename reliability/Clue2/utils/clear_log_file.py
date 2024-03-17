def clear_log_file(file_path):
    """Clear the contents of the specified log file."""
    try:
        with open(file_path, 'w') as file:
            file.truncate(0)  # Clear the contents of the file
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to access file '{file_path}'.")
    except Exception as e:
        print(f"Error: Failed to clear log file '{file_path}': {e}")
