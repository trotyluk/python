#!python3
import os
import sys
def sort_directories(path):
    try:
        # List all directories in the given path
        dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        
        # Sort directories by their names
        sorted_dirs = sorted(dirs)
        
        # Print sorted directories
        for d in sorted_dirs:
            print(d)
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
