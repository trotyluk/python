#!python3
import os
import sys
def move_folder(src,path1):
    # This function is a placeholder for moving folders to new folder named by First letter.
    print(src)
    f_letter = src[0].upper()
    new_folder = os.path.join(path1, f_letter)
    print(f_letter, new_folder)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    new_path = os.path.join(new_folder, src)
    os.rename(os.path.join(path1, src), new_path)
    
    
def sort_directories(path):   
    try:
        # List all directories in the given path
        dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        
        # Sort directories by their names
        sorted_dirs = sorted(dirs)
        
        # Print sorted directories
        for d in sorted_dirs:
            move_folder(d,path)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sort_dirs.py <path_to_directory>", file=sys.stderr)
        sys.exit(1)
    
    directory_path = sys.argv[1]
    sort_directories(directory_path)
    sys.exit(0)
# sort_dirs.py - A script to sort directories by their names in a given path.
# Usage: python sort_dirs.py <path_to_directory>
# It lists all directories in the specified path and prints them in sorted order.
