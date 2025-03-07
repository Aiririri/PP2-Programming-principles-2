# Write a Python program to list only directories, files and all directories, files in a specified path.
import os
import string


def list_contents(path):
    try:
        all_items = os.listdir(path)
        directories = [d for d in all_items if os.path.isdir(os.path.join(path, d))]
        files = [f for f in all_items if os.path.isfile(os.path.join(path, f))]
        
        print("Directories:")
        print("\n".join(directories) if directories else "No directories found")
        
        print("\nFiles:")
        print("\n".join(files) if files else "No files found")
        
        print("\nAll Items:")
        print("\n".join(all_items) if all_items else "No items found")
    
    except FileNotFoundError:
        print("The specified path does not exist.")
    except PermissionError:
        print("Permission denied. Unable to access the specified path.")

if __name__ == "__main__":
    path = input("Enter the directory path: ")
    list_contents(path)

# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

def check_path_access(path):
    print(f"Checking access for: {path}\n")
    
    if os.path.exists(path):
        print("Path exists: Yes")
        print(f"Readable: {'Yes' if os.access(path, os.R_OK) else 'No'}")
        print(f"Writable: {'Yes' if os.access(path, os.W_OK) else 'No'}")
        print(f"Executable: {'Yes' if os.access(path, os.X_OK) else 'No'}")
    else:
        print("Path exists: No")

if __name__ == "__main__":
    path = input("Enter the path to check: ")
    check_path_access(path)

# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
def check_path_details(path):
    if os.path.exists(path):
        print(f"The path exists: {path}\n")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")
    else:
        print("The specified path does not exist.")

if __name__ == "__main__":
    path = input("Enter the path to check: ")
    check_path_details(path)
# Write a Python program to count the number of lines in a text file.

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = sum(1 for _ in file)
        print(f"Number of lines in '{file_path}': {line_count}")
    except FileNotFoundError:
        print("Error: The specified file does not exist.")
    except PermissionError:
        print("Error: Permission denied to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the text file path: ")
    count_lines_in_file(file_path)

# Write a Python program to write a list to a file.
def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(f"{item}\n")
        print(f"List successfully written to '{file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the file path to write the list: ")
    data_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]  
    write_list_to_file(file_path, data_list)

# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt


def generate_text_files():
    try:
        for letter in string.ascii_uppercase:
            file_name = f"{letter}.txt"
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(f"This is file {file_name}\n")
        print("26 text files (A.txt to Z.txt) successfully created.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_text_files()

# Write a Python program to copy the contents of a file to another file
def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r', encoding='utf-8') as source_file:
            content = source_file.read()
        
        with open(destination_path, 'w', encoding='utf-8') as destination_file:
            destination_file.write(content)
        
        print(f"Contents copied from '{source_path}' to '{destination_path}' successfully.")
    except FileNotFoundError:
        print("Error: The source file does not exist.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    source = input("Enter the source file path: ")
    destination = input("Enter the destination file path: ")
    copy_file(source, destination)

# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            try:
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
            except Exception as e:
                print(f"An error occurred while deleting the file: {e}")
        else:
            print("Error: No write permission to delete the file.")
    else:
        print("Error: The specified file does not exist.")

if __name__ == "__main__":
    file_path = input("Enter the file path to delete: ")
    delete_file(file_path)