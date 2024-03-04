import os
import re

# Function to search for a word in a file
def search_word_in_file(file_path, word, encoding='utf-8'):
    with open(file_path, 'rb') as file:
        for line_number, raw_line in enumerate(file, start=1):
            try:
                line = raw_line.decode(encoding)
                if re.search(r'\b{}\b'.format(re.escape(word)), line):
                    return True
            except UnicodeDecodeError:
                # Handle decoding errors
                print(f"Error decoding line {line_number} in {file_path}")
    return False

# Function to search for a word in all .js files in a directory
def search_word_in_directory(directory_path, word, encoding='utf-8'):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.js'):
                file_path = os.path.join(root, file)
                if search_word_in_file(file_path, word, encoding):
                    print(f'Found in {file_path}')

if __name__ == "__main__":
    directory_path = input("Enter the directory path to search in: ")
    word = input("Enter the word to search for: ")

    search_word_in_directory(directory_path, word)

