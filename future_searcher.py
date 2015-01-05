import os
import sys
import __future__

directory = sys.argv[1]
FUTURE_STUFF = dir(__future__)

def main():
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

        for file_path in files_with_future:
            print file_path
    else:
        print 'Directory not found!'


if __name__ == '__main__':
    main()
