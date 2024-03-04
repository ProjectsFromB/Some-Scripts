#!/bin/bash

# Check if the required arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <directory> <search_string>"
    exit 1
fi

directory="$1"
search_string="$2"

# Check if the provided directory exists
if [ ! -d "$directory" ]; then
    echo "Error: Directory '$directory' not found."
    exit 1
fi

# Use find to get a list of all files in the specified directory and its subdirectories
files=$(find "$directory" -type f)

# Loop through each file and use grep to search for the string
for file in $files; do
    # Use grep to search for the string in the file
    grep -q "$search_string" "$file"
    
    # Check the exit status of grep
    if [ $? -eq 0 ]; then
        echo "Found in file: $file"
    fi
done

echo "Search complete."

