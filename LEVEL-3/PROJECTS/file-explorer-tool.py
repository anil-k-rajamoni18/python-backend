import os
import datetime

def format_size(bytes_size):
    """Convert bytes to a human-readable format."""
    for unit in ['B','KB','MB','GB','TB']:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024
    return f"{bytes_size:.2f} PB"

def format_date(timestamp):
    """Convert timestamp to readable date."""
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def list_directory(path):
    """List files and directories with details."""
    try:
        items = os.listdir(path)
    except FileNotFoundError:
        print("Error: Folder not found.")
        return None
    except PermissionError:
        print("Error: Permission denied.")
        return None

    if not items:
        print("Folder is empty.")
        return []

    print(f"\nContents of folder: {path}")
    file_info = []
    for i, item in enumerate(items, start=1):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            ctime = os.path.getctime(full_path)
            print(f"{i}. [FILE] {item} - Size: {format_size(size)}, Created: {format_date(ctime)}")
            file_info.append((item, 'file', full_path))
        elif os.path.isdir(full_path):
            print(f"{i}. [DIR ] {item}")
            file_info.append((item, 'dir', full_path))
        else:
            print(f"{i}. [UNK ] {item}")
            file_info.append((item, 'unknown', full_path))
    return file_info

def view_file(filepath):
    """Display the contents of a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            print(f"\n--- Contents of '{os.path.basename(filepath)}' ---")
            for line in f:
                print(line, end='')
            print("\n--- End of file ---\n")
    except Exception as e:
        print(f"Could not read file: {e}")

def delete_file(filepath):
    """Delete a file after user confirmation."""
    confirm = input(f"Are you sure you want to delete '{os.path.basename(filepath)}'? (y/n): ").strip().lower()
    if confirm == 'y':
        try:
            os.remove(filepath)
            print("File deleted successfully.")
        except Exception as e:
            print(f"Failed to delete file: {e}")
    else:
        print("Deletion cancelled.")

def main():
    folder = input("Enter folder path to explore: ").strip()
    file_list = list_directory(folder)
    if not file_list:
        return

    while True:
        choice = input("\nEnter the number of a file to view/delete, or 'q' to quit: ").strip()
        if choice.lower() == 'q':
            print("Exiting File Explorer.")
            break

        if not choice.isdigit():
            print("Invalid input. Please enter a valid number or 'q' to quit.")
            continue

        index = int(choice) - 1
        if index < 0 or index >= len(file_list):
            print("Invalid number. Please try again.")
            continue

        name, ftype, full_path = file_list[index]

        if ftype == 'dir':
            print(f"'{name}' is a directory. Please select a file to view or delete.")
            continue
        elif ftype == 'file':
            action = input(f"Do you want to (v)iew or (d)elete '{name}'? ").strip().lower()
            if action == 'v':
                view_file(full_path)
            elif action == 'd':
                delete_file(full_path)
                # Refresh the file list after deletion
                file_list = list_directory(folder)
                if not file_list:
                    break
            else:
                print("Invalid action. Please enter 'v' or 'd'.")
        else:
            print(f"Unknown item type for '{name}'.")

if __name__ == "__main__":
    main()
