def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile Content:")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist")

def read_file_line_by_line(filename):
    try:
        with open(filename, 'r') as file:
            print("\nFile Content (Line by Line):")
            line = file.readline()
            while line:
                print(line, end='')  # 'end' to avoid extra newlines
                line = file.readline()
    except FileNotFoundError:
        print("Error: The file does not exist")

def read_file_with_readlines(filename):
    try:
        with open(filename, 'r') as file:
            print("\nFile Content (Using readlines):")
            lines = file.readlines()
            for line in lines:
                print(line, end='')  # 'end' to avoid extra newlines
    except FileNotFoundError:
        print("Error: The fi
            le does not exist")

def write_file_overwrite(filename):
    content = input("\nEnter the content to overwrite in the file: ")
    with open(filename, 'w') as file:
        file.write(content)
    print("File has been overwritten with the new content.")

def write_file_append(filename):
    content = input("\nEnter the content to append to the file: ")
    with open(filename, 'a') as file:
        file.write(content + '\n')  # Append with a newline
    print("Content has been appended to the file.")

def main():
    filename = input("Enter the (.txt) file name: ")
    while True:
        print("\nChoose an option:")
        print("1. Read the entire file")
        print("2. Read the file line by line")
        print("3. Read the file using readlines")
        print("4. Overwrite content in the file")
        print("5. Append content to the file")
        print("6. Exit")

        # Get user choice
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            read_file(filename)
        elif choice == '2':
            read_file_line_by_line(filename)
        elif choice == '3':
            read_file_with_readlines(filename)
        elif choice == '4':
            write_file_overwrite(filename)
        elif choice == '5':
            write_file_append(filename)
        elif choice == '6':
            print("mudichu vitinga!")
            break  # Exit the loop and end the program
        else:
            print("Invalid option! Please try again.")

# Directly call the main function to start the program
main()

