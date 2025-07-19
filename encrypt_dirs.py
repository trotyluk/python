import os
import subprocess
import shutil

def compress_directory(directory, delete_dirs=False):
    # Get the list of all directories in the provided directory
    dirs = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

    # Initialize counter for archive naming
    count = 1

    # Iterate over each directory and compress it
    for dir_name in dirs:
        dir_path = os.path.join(directory, dir_name)

        # Create the output archive name
        output_archive = f"{os.path.splitext(dir_name)[0]}{count:03d}.7z"

        # Command to create a 7z archive with encryption and headers
        command = [
            '7z', 'a', '-pYourPassword', '-mx=9', '-t7z', '-mhe=on',
            output_archive, dir_path
        ]

        try:
            # Execute the command using subprocess
            result = subprocess.run(command, check=True)
            print(f"Successfully compressed {dir_name} to {output_archive}")

            # Check if the archive exists
            if not os.path.exists(output_archive):
                print(f"Failed to create archive for {dir_name}")
                continue

            # Optionally, remove the original directory if successful (use with caution)
            if delete_dirs:
                shutil.rmtree(dir_path)
                print(f"Deleted original directory: {dir_path}")

        except subprocess.CalledProcessError as e:
            print(f"Failed to compress {dir_name}: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Compress all directories in a provided directory.')
    parser.add_argument('directory', type=str, help='The directory containing subdirectories to compress')
    parser.add_argument('--delete', '-d', action='store_true', help='Delete original directories after compression')

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Provided path {args.directory} is not a valid directory.")
        exit(1)

    compress_directory(args.directory, delete_dirs=args.delete)
```

### How to Use the Script

1. **Save the script** as `compress_dirs.py`.
2. **Make sure 7-Zip** is installed on your system and accessible from your command line.
3. **Run the script** with a directory path as an argument:
   ```sh
   python compress_dirs.py /path/to/your/directory --delete
   ```
4. **Replace `YourPassword`** in the script with your actual password.

### Explanation

- The script uses the `argparse` module to accept a command-line argument for the directory containing subdirectories.
- It includes an optional switch `--delete` (or `-d`) that, when provided, will delete the original directories after successful compression.
- The function `compress_directory()` now takes an additional parameter `delete_dirs`, which is set based on whether the `--delete` flag was passed.

### Notes

- The script assumes that 7-Zip is installed and available in your system's PATH.
- You can optionally remove the original directories after successful compression by using the `--delete` or `-d` switch. Be cautious as this will permanently delete the
directories.