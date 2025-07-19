import os
import shutil

def compress_directory(directory, delete_dirs=False):
    # Get the list of all directories in the provided directory
    dirs = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

    # Initialize counter for archive naming
    count = 1

    # Iterate over each directory and compress it
    for dir_name in dirs:
        dir_path = os.path.join(directory, dir_name)

        # Create the output archive name using the parent directory's name and sequence number
        parent_dir = os.path.basename(directory)
        output_archive = f"{parent_dir}_{count:03d}.7z"
        

        # Command to create a 7z archive with encryption and headers
        command = '7z a -pAla@ma@kota3472 "'+ output_archive +'" "'+ dir_path + '"'
        # command = [
        #     '7z', 'a', '-pTrotyl3472', '-mx=9', '-t7z', '-mhe=on',
        #     'output_archive, dir_path
        # ]
        
#  create7z = '7z a -pAla@ma@kota3472 "'+ archname +'.7z" "'+ archname + '"'
#     # print(f'Creating {archname}.7z')
#     os.system(create7z)
        try:
            # Execute the command using os.system
            result = os.system(command)
            print(command)

            if result == 0:
                print(f"Successfully compressed {dir_name} to {output_archive}")
                # Increase counter only if compression was successful
                count += 1
                # Optionally, remove the original directory if successful (use with caution)
                if delete_dirs:
                    shutil.rmtree(dir_path)
                    print(f"Deleted original directory: {dir_path}")
            

            else:
                raise Exception("Command execution failed")

        except Exception as e:
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