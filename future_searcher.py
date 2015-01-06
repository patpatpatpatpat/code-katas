import os
import sys

directory = sys.argv[1] if len(sys.argv) > 1 else ''


def get_files_using_future(directory):
    """
    Returns list of file paths of python files under `directory` that uses __future__

    Returns an empty list if directory does not exist or no python files were using __future__
    """
    files_with_future = []

    if os.path.exists(directory):
        for (dirpath, dirnames, filenames) in os.walk(directory):
            python_files = [
                python_file
                for python_file in filenames
                if python_file.endswith('.py')
            ]

            for python_file in python_files:
                file_path = os.path.join(dirpath, python_file)

                with open(file_path) as file_data:
                    data = file_data.read()

                    if '__future__' in data:
                        files_with_future.append(file_path)
                        file_data.close()
                        break

    return files_with_future if files_with_future else []


def main():
    files_with_future = get_files_using_future(directory)

    if files_with_future:
        print "Files using __future__"
        for file_path in files_with_future:
            print file_path
    else:
        print "Directory not found or no files using __future__!"


if __name__ == '__main__':
    main()
