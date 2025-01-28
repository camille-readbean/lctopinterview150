import argparse

def read_and_modify_file(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the contents of the file
            content = file.read()

            # Replace all newline characters with a literal '\n'
            modified_content = content.replace('\n', '\\n')

        # Print the modified content
        print(modified_content)
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Modify newline characters in a file.')
    parser.add_argument('file_path', type=str, help='Path to the file')

    args = parser.parse_args()

    read_and_modify_file(args.file_path)