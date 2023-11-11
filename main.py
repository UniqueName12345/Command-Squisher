
import argparse

def squish(command):
    # Use replace() method to replace backslashes and newlines with a space
    command = command.replace('\\\n', ' ')
    return command


import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-stdin", action="store_true", help="If given, ask for the command directly")
    args = parser.parse_args()

    if args.stdin:
        command = input("Enter the command: ")
    else:
        file_path = input("Enter the path to the file: ")
        with open(file_path, "r") as file:
            command = file.read()

    return command

command = parse_arguments()
command = squish(command)
print(command)